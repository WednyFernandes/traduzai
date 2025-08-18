#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TraduzAI CSV - Interface Gráfica para Tradução de Arquivos CSV
Autor: Wedny Fernandes
Data: 2025-08-17

Interface gráfica amigável para tradução automatizada de arquivos CSV
usando Google Translate com preservação de formatação.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import csv
import re
import json
import os
import sys
import threading
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from datetime import datetime
import queue

try:
    from googletrans import Translator, LANGUAGES
    GOOGLETRANS_AVAILABLE = True
except ImportError:
    GOOGLETRANS_AVAILABLE = False

@dataclass
class TranslationConfig:
    """Configurações para tradução"""
    source_language: str = 'pt'
    target_language: str = 'en'
    currency_symbol: str = '$'
    convert_currency: bool = False
    currency_conversion_rate: float = 1.0
    preserve_numbers: bool = True
    preserve_urls: bool = True
    preserve_emails: bool = True
    max_retries: int = 3

class CSVTranslatorGUI:
    """Interface gráfica para tradução de CSV"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("TraduzAI CSV - Tradutor de Arquivos CSV")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Variáveis
        self.csv_file_path = tk.StringVar()
        self.source_lang = tk.StringVar(value='pt')
        self.target_lang = tk.StringVar(value='en')
        self.output_file_path = tk.StringVar()
        self.progress_var = tk.DoubleVar()
        self.status_var = tk.StringVar(value="Pronto para traduzir")
        
        # Configurações avançadas
        self.preserve_numbers = tk.BooleanVar(value=True)
        self.preserve_urls = tk.BooleanVar(value=True)
        self.preserve_emails = tk.BooleanVar(value=True)
        self.convert_currency = tk.BooleanVar(value=False)
        self.currency_symbol = tk.StringVar(value="$")
        self.currency_rate = tk.DoubleVar(value=1.0)
        
        # Queue para comunicação entre threads
        self.progress_queue = queue.Queue()
        
        # Translator
        self.translator = None
        if GOOGLETRANS_AVAILABLE:
            self.translator = Translator()
        
        self.setup_ui()
        self.check_dependencies()
        
    def check_dependencies(self):
        """Verifica se as dependências estão instaladas"""
        if not GOOGLETRANS_AVAILABLE:
            messagebox.showerror(
                "Erro de Dependência",
                "A biblioteca 'googletrans' não está instalada.\n\n"
                "Execute: pip install googletrans==4.0.0rc1\n\n"
                "O programa será fechado."
            )
            self.root.destroy()
            return
            
    def setup_ui(self):
        """Configura a interface do usuário"""
        # Estilo
        style = ttk.Style()
        style.theme_use('clam')
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Título
        title_label = ttk.Label(main_frame, text="TraduzAI CSV - Tradutor de Arquivos", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Seleção de arquivo
        ttk.Label(main_frame, text="Arquivo CSV:").grid(row=1, column=0, sticky=tk.W, pady=5)
        ttk.Entry(main_frame, textvariable=self.csv_file_path, width=50).grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 5))
        ttk.Button(main_frame, text="Selecionar", command=self.select_file).grid(row=1, column=2, pady=5)
        
        # Frame para idiomas
        lang_frame = ttk.LabelFrame(main_frame, text="Configurações de Idioma", padding="10")
        lang_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        lang_frame.columnconfigure(1, weight=1)
        lang_frame.columnconfigure(3, weight=1)
        
        # Idioma origem
        ttk.Label(lang_frame, text="Idioma Origem:").grid(row=0, column=0, sticky=tk.W, pady=5)
        source_combo = ttk.Combobox(lang_frame, textvariable=self.source_lang, width=20)
        source_combo.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 20))
        
        # Idioma destino
        ttk.Label(lang_frame, text="Idioma Destino:").grid(row=0, column=2, sticky=tk.W, pady=5)
        target_combo = ttk.Combobox(lang_frame, textvariable=self.target_lang, width=20)
        target_combo.grid(row=0, column=3, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Configurar comboboxes com idiomas
        if GOOGLETRANS_AVAILABLE:
            languages = [(code, name.title()) for code, name in LANGUAGES.items()]
            languages.sort(key=lambda x: x[1])
            lang_values = [f"{code} - {name}" for code, name in languages]
            
            source_combo['values'] = lang_values
            target_combo['values'] = lang_values
            
            # Definir valores padrão
            source_combo.set("pt - Portuguese")
            target_combo.set("en - English")
        
        # Frame para configurações avançadas
        advanced_frame = ttk.LabelFrame(main_frame, text="Configurações Avançadas", padding="10")
        advanced_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        
        # Checkboxes para preservação
        ttk.Checkbutton(advanced_frame, text="Preservar números", 
                       variable=self.preserve_numbers).grid(row=0, column=0, sticky=tk.W)
        ttk.Checkbutton(advanced_frame, text="Preservar URLs", 
                       variable=self.preserve_urls).grid(row=0, column=1, sticky=tk.W)
        ttk.Checkbutton(advanced_frame, text="Preservar emails", 
                       variable=self.preserve_emails).grid(row=0, column=2, sticky=tk.W)
        
        # Configurações de moeda
        currency_frame = ttk.Frame(advanced_frame)
        currency_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))
        
        ttk.Checkbutton(currency_frame, text="Converter moeda", 
                       variable=self.convert_currency).grid(row=0, column=0, sticky=tk.W)
        ttk.Label(currency_frame, text="Símbolo:").grid(row=0, column=1, sticky=tk.W, padx=(20, 5))
        ttk.Entry(currency_frame, textvariable=self.currency_symbol, width=5).grid(row=0, column=2, sticky=tk.W)
        ttk.Label(currency_frame, text="Taxa:").grid(row=0, column=3, sticky=tk.W, padx=(20, 5))
        ttk.Entry(currency_frame, textvariable=self.currency_rate, width=10).grid(row=0, column=4, sticky=tk.W)
        
        # Arquivo de saída
        ttk.Label(main_frame, text="Arquivo de Saída:").grid(row=4, column=0, sticky=tk.W, pady=5)
        ttk.Entry(main_frame, textvariable=self.output_file_path, width=50).grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 5))
        ttk.Button(main_frame, text="Selecionar", command=self.select_output_file).grid(row=4, column=2, pady=5)
        
        # Barra de progresso
        progress_frame = ttk.Frame(main_frame)
        progress_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=20)
        progress_frame.columnconfigure(0, weight=1)
        
        self.progress_bar = ttk.Progressbar(progress_frame, variable=self.progress_var, 
                                          maximum=100, length=400)
        self.progress_bar.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        # Status
        status_label = ttk.Label(main_frame, textvariable=self.status_var)
        status_label.grid(row=6, column=0, columnspan=3, pady=5)
        
        # Botões
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=7, column=0, columnspan=3, pady=20)
        
        self.translate_button = ttk.Button(button_frame, text="Iniciar Tradução", 
                                         command=self.start_translation, style='Accent.TButton')
        self.translate_button.pack(side=tk.LEFT, padx=(0, 10))
        
        ttk.Button(button_frame, text="Limpar", command=self.clear_fields).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(button_frame, text="Sair", command=self.root.quit).pack(side=tk.LEFT)
        
        # Log area
        log_frame = ttk.LabelFrame(main_frame, text="Log de Tradução", padding="5")
        log_frame.grid(row=8, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(20, 0))
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        
        self.log_text = scrolledtext.ScrolledText(log_frame, height=8, width=80)
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar expansão
        main_frame.rowconfigure(8, weight=1)
        
    def select_file(self):
        """Seleciona arquivo CSV de entrada"""
        filename = filedialog.askopenfilename(
            title="Selecionar arquivo CSV",
            filetypes=[("Arquivos CSV", "*.csv"), ("Todos os arquivos", "*.*")]
        )
        if filename:
            self.csv_file_path.set(filename)
            # Sugerir nome do arquivo de saída
            base_name = os.path.splitext(filename)[0]
            target_code = self.target_lang.get().split(' - ')[0] if ' - ' in self.target_lang.get() else self.target_lang.get()
            suggested_output = f"{base_name}_traduzido_{target_code}.csv"
            self.output_file_path.set(suggested_output)
            
    def select_output_file(self):
        """Seleciona arquivo CSV de saída"""
        filename = filedialog.asksaveasfilename(
            title="Salvar arquivo traduzido como",
            defaultextension=".csv",
            filetypes=[("Arquivos CSV", "*.csv"), ("Todos os arquivos", "*.*")]
        )
        if filename:
            self.output_file_path.set(filename)
            
    def clear_fields(self):
        """Limpa todos os campos"""
        self.csv_file_path.set("")
        self.output_file_path.set("")
        self.progress_var.set(0)
        self.status_var.set("Pronto para traduzir")
        self.log_text.delete(1.0, tk.END)
        
    def log_message(self, message):
        """Adiciona mensagem ao log"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()
        
    def validate_inputs(self):
        """Valida as entradas do usuário"""
        if not self.csv_file_path.get():
            messagebox.showerror("Erro", "Selecione um arquivo CSV de entrada")
            return False
            
        if not os.path.exists(self.csv_file_path.get()):
            messagebox.showerror("Erro", "Arquivo CSV de entrada não encontrado")
            return False
            
        if not self.output_file_path.get():
            messagebox.showerror("Erro", "Especifique um arquivo de saída")
            return False
            
        # Extrair códigos de idioma
        source = self.source_lang.get().split(' - ')[0] if ' - ' in self.source_lang.get() else self.source_lang.get()
        target = self.target_lang.get().split(' - ')[0] if ' - ' in self.target_lang.get() else self.target_lang.get()
        
        if source == target:
            messagebox.showerror("Erro", "Idioma de origem e destino devem ser diferentes")
            return False
            
        return True
        
    def start_translation(self):
        """Inicia o processo de tradução em thread separada"""
        if not self.validate_inputs():
            return
            
        # Desabilitar botão
        self.translate_button.config(state='disabled')
        self.progress_var.set(0)
        self.status_var.set("Iniciando tradução...")
        self.log_text.delete(1.0, tk.END)
        
        # Iniciar thread de tradução
        thread = threading.Thread(target=self.translate_csv, daemon=True)
        thread.start()
        
        # Iniciar monitoramento de progresso
        self.root.after(100, self.check_progress)
        
    def check_progress(self):
        """Verifica atualizações de progresso da thread"""
        try:
            while True:
                message = self.progress_queue.get_nowait()
                if message['type'] == 'progress':
                    self.progress_var.set(message['value'])
                elif message['type'] == 'status':
                    self.status_var.set(message['value'])
                elif message['type'] == 'log':
                    self.log_message(message['value'])
                elif message['type'] == 'complete':
                    self.progress_var.set(100)
                    self.status_var.set("Tradução concluída!")
                    self.translate_button.config(state='normal')
                    messagebox.showinfo("Sucesso", f"Arquivo traduzido salvo em:\n{self.output_file_path.get()}")
                    return
                elif message['type'] == 'error':
                    self.status_var.set("Erro na tradução")
                    self.translate_button.config(state='normal')
                    messagebox.showerror("Erro", message['value'])
                    return
        except queue.Empty:
            pass
        
        # Continuar verificando
        self.root.after(100, self.check_progress)
        
    def translate_csv(self):
        """Função de tradução executada em thread separada"""
        try:
            # Configurar tradutor
            config = TranslationConfig(
                source_language=self.source_lang.get().split(' - ')[0] if ' - ' in self.source_lang.get() else self.source_lang.get(),
                target_language=self.target_lang.get().split(' - ')[0] if ' - ' in self.target_lang.get() else self.target_lang.get(),
                currency_symbol=self.currency_symbol.get(),
                convert_currency=self.convert_currency.get(),
                currency_conversion_rate=self.currency_rate.get(),
                preserve_numbers=self.preserve_numbers.get(),
                preserve_urls=self.preserve_urls.get(),
                preserve_emails=self.preserve_emails.get()
            )
            
            self.progress_queue.put({'type': 'log', 'value': f'Iniciando tradução de {config.source_language} para {config.target_language}'})
            
            # Ler arquivo CSV
            with open(self.csv_file_path.get(), 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                rows = list(reader)
                
            if len(rows) < 2:
                raise ValueError("O arquivo CSV deve ter pelo menos 2 linhas (cabeçalho + dados)")
                
            self.progress_queue.put({'type': 'log', 'value': f'Arquivo lido: {len(rows)} linhas encontradas'})
            
            # Cabeçalho e dados originais
            header = rows[0]
            original_data = rows[1]
            
            # Traduzir dados
            translated_data = []
            total_fields = len(original_data)
            
            for i, field in enumerate(original_data):
                progress = (i / total_fields) * 100
                self.progress_queue.put({'type': 'progress', 'value': progress})
                self.progress_queue.put({'type': 'status', 'value': f'Traduzindo campo {i+1} de {total_fields}'})
                
                if field.strip():
                    translated_field = self.translate_text(field, config)
                    translated_data.append(translated_field)
                    self.progress_queue.put({'type': 'log', 'value': f'Campo {i+1}: "{field}" → "{translated_field}"'})
                else:
                    translated_data.append(field)
                    
            # Salvar arquivo
            self.progress_queue.put({'type': 'status', 'value': 'Salvando arquivo...'})
            
            with open(self.output_file_path.get(), 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file, quoting=csv.QUOTE_ALL)
                writer.writerow(header)
                writer.writerow(original_data)
                writer.writerow(translated_data)
                
            self.progress_queue.put({'type': 'log', 'value': f'Arquivo salvo: {self.output_file_path.get()}'})
            self.progress_queue.put({'type': 'complete', 'value': True})
            
        except Exception as e:
            self.progress_queue.put({'type': 'error', 'value': str(e)})
            
    def translate_text(self, text, config):
        """Traduz um texto individual"""
        try:
            # Garantir que text é string
            text_str = str(text).strip()
            
            if not text_str:
                return text_str
            
            # Preservar elementos
            clean_text, placeholders = self.preserve_elements(text_str, config)
            
            # Detectar padrão de caixa
            case_pattern = self.detect_case_pattern(clean_text)
            
            # Traduzir
            if clean_text.strip():
                result = self.translator.translate(clean_text, 
                                                 src=config.source_language, 
                                                 dest=config.target_language)
                translated = result.text
            else:
                translated = clean_text
                
            # Aplicar padrão de caixa
            translated = self.apply_case_pattern(translated, case_pattern)
            
            # Restaurar elementos
            translated = self.restore_elements(translated, placeholders)
            
            # Converter moeda se necessário
            if config.convert_currency:
                translated = self.convert_currency(translated, config)
                
            return translated
            
        except Exception as e:
            self.progress_queue.put({'type': 'log', 'value': f'Erro ao traduzir "{text}": {str(e)}'})
            return str(text)  # Retornar o texto original como string
            
    def preserve_elements(self, text, config):
        """Preserva elementos específicos do texto"""
        placeholders = {}
        modified_text = str(text)  # Garantir que é string
        counter = 0
        
        patterns = {
            'url': re.compile(r'https?://[^\s<>"]+|www\.[^\s<>"]+', re.IGNORECASE),
            'email': re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
            'number': re.compile(r'\b\d+(?:[,\.]\d+)*\b')
        }
        
        # Preservar URLs
        if config.preserve_urls:
            for match in patterns['url'].finditer(modified_text):
                placeholder = f"__URL_{counter}__"
                placeholders[placeholder] = match.group()
                modified_text = modified_text.replace(match.group(), placeholder)
                counter += 1
        
        # Preservar emails
        if config.preserve_emails:
            for match in patterns['email'].finditer(modified_text):
                placeholder = f"__EMAIL_{counter}__"
                placeholders[placeholder] = match.group()
                modified_text = modified_text.replace(match.group(), placeholder)
                counter += 1
        
        # Preservar números
        if config.preserve_numbers:
            for match in patterns['number'].finditer(modified_text):
                if not any(match.group() in value for value in placeholders.values()):
                    placeholder = f"__NUMBER_{counter}__"
                    placeholders[placeholder] = match.group()
                    modified_text = modified_text.replace(match.group(), placeholder)
                    counter += 1
        
        return modified_text, placeholders
        
    def detect_case_pattern(self, text):
        """Detecta o padrão de caixa do texto"""
        text_str = str(text)  # Garantir que é string
        if text_str.isupper():
            return "UPPER"
        elif text_str.islower():
            return "LOWER"
        elif text_str.istitle():
            return "TITLE"
        else:
            return "MIXED"
            
    def apply_case_pattern(self, text, pattern):
        """Aplica o padrão de caixa ao texto"""
        text_str = str(text)  # Garantir que é string
        if pattern == "UPPER":
            return text_str.upper()
        elif pattern == "LOWER":
            return text_str.lower()
        elif pattern == "TITLE":
            return text_str.title()
        else:
            return text_str
            
    def restore_elements(self, text, placeholders):
        """Restaura elementos preservados"""
        restored_text = str(text)  # Garantir que é string
        for placeholder, original_value in placeholders.items():
            restored_text = restored_text.replace(placeholder, str(original_value))
        return restored_text
        
    def convert_currency(self, text, config):
        """Converte valores monetários"""
        text_str = str(text)  # Garantir que é string
        currency_pattern = re.compile(r'(\d+(?:[,\.]\d+)*(?:[,\.]\d{2})?)\s*(?:R\$|BRL|reais?)?', re.IGNORECASE)
        
        def currency_replacer(match):
            value_str = match.group(1)
            # Normalizar e converter
            normalized = value_str.replace(',', '.')
            try:
                value = float(normalized) * config.currency_conversion_rate
                return f"{config.currency_symbol}{value:.2f}"
            except ValueError:
                return match.group(0)
                
        return currency_pattern.sub(currency_replacer, text_str)

def main():
    """Função principal"""
    root = tk.Tk()
    
    # Configurar ícone se disponível
    try:
        root.iconbitmap("icon.ico")
    except:
        pass
        
    app = CSVTranslatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
