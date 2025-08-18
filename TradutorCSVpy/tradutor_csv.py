#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tradutor CSV - Script para tradução e localização de textos em arquivos CSV
Autor: GitHub Copilot
Data: 2025-08-17

Este script permite traduzir textos em arquivos CSV mantendo:
- Estrutura original do CSV
- Padrões de pontuação e aspas
- Formatação de valores monetários
- Opções de conversão de valores numéricos
"""

import csv
import re
import json
import argparse
import os
import sys
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from datetime import datetime

try:
    from googletrans import Translator
    GOOGLETRANS_AVAILABLE = True
except ImportError:
    GOOGLETRANS_AVAILABLE = False
    print("⚠️  Aviso: googletrans não está instalado. Execute: pip install googletrans==4.0.0rc1")

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

class CSVTranslator:
    """Classe principal para tradução de arquivos CSV"""
    
    def __init__(self, config: TranslationConfig):
        self.config = config
        self.translator = None
        self.translation_cache = {}
        self.patterns = self._compile_patterns()
        
        if GOOGLETRANS_AVAILABLE:
            self.translator = Translator()
    
    def _compile_patterns(self) -> Dict[str, re.Pattern]:
        """Compila padrões regex para preservar elementos específicos"""
        return {
            'currency': re.compile(r'(\d+(?:[,\.]\d+)*(?:[,\.]\d{2})?)\s*(?:R\$|BRL|reais?)?', re.IGNORECASE),
            'number': re.compile(r'\b\d+(?:[,\.]\d+)*\b'),
            'url': re.compile(r'https?://[^\s<>"]+|www\.[^\s<>"]+', re.IGNORECASE),
            'email': re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
            'quotes': re.compile(r'["""\'\'`]'),
            'punctuation': re.compile(r'[\.!?;:,\-—–…]'),
            'parentheses': re.compile(r'[\(\)\[\]{}]'),
        }
    
    def _preserve_elements(self, text: str) -> Tuple[str, Dict[str, str]]:
        """
        Preserva elementos específicos do texto substituindo por placeholders
        Retorna o texto modificado e um dicionário de mapeamento
        """
        placeholders = {}
        modified_text = text
        counter = 0
        
        # Preservar URLs
        if self.config.preserve_urls:
            for match in self.patterns['url'].finditer(text):
                placeholder = f"__URL_{counter}__"
                placeholders[placeholder] = match.group()
                modified_text = modified_text.replace(match.group(), placeholder)
                counter += 1
        
        # Preservar emails
        if self.config.preserve_emails:
            for match in self.patterns['email'].finditer(modified_text):
                placeholder = f"__EMAIL_{counter}__"
                placeholders[placeholder] = match.group()
                modified_text = modified_text.replace(match.group(), placeholder)
                counter += 1
        
        # Preservar números se configurado
        if self.config.preserve_numbers:
            for match in self.patterns['number'].finditer(modified_text):
                # Verificar se não é parte de uma URL ou email já preservada
                if not any(match.group() in value for value in placeholders.values()):
                    placeholder = f"__NUMBER_{counter}__"
                    placeholders[placeholder] = match.group()
                    modified_text = modified_text.replace(match.group(), placeholder)
                    counter += 1
        
        return modified_text, placeholders
    
    def _detect_case_pattern(self, text: str) -> str:
        """Detecta o padrão de caixa do texto original"""
        if text.isupper():
            return "UPPER"
        elif text.islower():
            return "LOWER"
        elif text.istitle():
            return "TITLE"
        else:
            return "MIXED"
    
    def _apply_case_pattern(self, translated_text: str, original_pattern: str) -> str:
        """Aplica o padrão de caixa do texto original ao texto traduzido"""
        if original_pattern == "UPPER":
            return translated_text.upper()
        elif original_pattern == "LOWER":
            return translated_text.lower()
        elif original_pattern == "TITLE":
            return translated_text.title()
        else:
            return translated_text
    
    def _preserve_csv_quotes(self, text: str) -> Tuple[str, bool]:
        """Preserva aspas e formatação CSV"""
        # Verificar se o texto está entre aspas
        if text.startswith('"') and text.endswith('"'):
            # Remover aspas para tradução, mas lembrar de recolocar
            return text[1:-1], True
        return text, False
    
    def _restore_elements(self, translated_text: str, placeholders: Dict[str, str]) -> str:
        """Restaura elementos preservados no texto traduzido"""
        restored_text = translated_text
        
        for placeholder, original_value in placeholders.items():
            restored_text = restored_text.replace(placeholder, original_value)
        
        return restored_text
    
    def _convert_currency(self, text: str) -> str:
        """Converte valores monetários conforme configuração"""
        def currency_replacer(match):
            value_str = match.group(1)
            
            # Normalizar formato de número (converter vírgula para ponto)
            normalized_value = value_str.replace(',', '.')
            
            try:
                value = float(normalized_value)
                
                if self.config.convert_currency:
                    converted_value = value * self.config.currency_conversion_rate
                    return f"{self.config.currency_symbol}{converted_value:.2f}"
                else:
                    # Apenas trocar símbolo, manter formato original
                    return f"{self.config.currency_symbol}{value_str}"
                    
            except ValueError:
                # Se não conseguir converter, mantém original com novo símbolo
                return f"{self.config.currency_symbol}{value_str}"
        
        return self.patterns['currency'].sub(currency_replacer, text)
    
    def _handle_currency_in_text(self, text: str) -> str:
        """Trata especificamente valores monetários no texto"""
        # Padrão mais específico para valores monetários
        currency_pattern = re.compile(r'(\d+(?:[,\.]\d+)*(?:[,\.]\d{2})?)')
        
        # Se há um padrão de preço (números isolados que parecem preços)
        if currency_pattern.search(text) and len(text.strip()) < 20:  # Provavelmente um preço
            return self._convert_currency(text)
        
        return text
    
    def _translate_text(self, text: str) -> str:
        """Traduz um texto individual"""
        if not text or not text.strip():
            return text
        
        # Verificar se é provável que seja um preço
        is_likely_price = (re.match(r'^\s*\d+(?:[,\.]\d+)*(?:[,\.]\d{2})?\s*$', text.strip()) is not None)
        
        if is_likely_price:
            return self._handle_currency_in_text(text)
        
        # Detectar se o texto inteiro está em caixa alta
        is_all_uppercase = text.isupper()
        
        # Verificar cache
        cache_key = f"{text}_{self.config.source_language}_{self.config.target_language}"
        if cache_key in self.translation_cache:
            result = self.translation_cache[cache_key]
            # Aplicar caixa alta se necessário
            return result.upper() if is_all_uppercase else result
        
        if not GOOGLETRANS_AVAILABLE or not self.translator:
            print(f"⚠️  Tradução não disponível para: {text[:50]}...")
            return text
        
        # Preservar elementos específicos
        modified_text, placeholders = self._preserve_elements(text)
        
        try:
            # Tentar traduzir com retry
            for attempt in range(self.config.max_retries):
                try:
                    result = self.translator.translate(
                        modified_text,
                        src=self.config.source_language,
                        dest=self.config.target_language
                    )
                    
                    if result and result.text:
                        translated = result.text
                        break
                        
                except Exception as e:
                    if attempt == self.config.max_retries - 1:
                        print(f"❌ Erro na tradução após {self.config.max_retries} tentativas: {e}")
                        return text
                    else:
                        print(f"⚠️  Tentativa {attempt + 1} falhou, tentando novamente...")
                        continue
            else:
                return text
            
            # Restaurar elementos preservados
            translated = self._restore_elements(translated, placeholders)
            
            # Aplicar caixa alta se o texto original estava todo em maiúscula
            if is_all_uppercase:
                translated = translated.upper()
            
            # Converter moedas se necessário
            translated = self._handle_currency_in_text(translated)
            
            # Armazenar no cache
            self.translation_cache[cache_key] = translated
            
            return translated
            
        except Exception as e:
            print(f"❌ Erro na tradução: {e}")
            return text
    
    def translate_csv(self, input_file: str, output_file: str = None) -> str:
        """
        Traduz um arquivo CSV completo
        
        Args:
            input_file: Caminho do arquivo CSV de entrada
            output_file: Caminho do arquivo CSV de saída (opcional)
        
        Returns:
            Caminho do arquivo de saída criado
        """
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Arquivo não encontrado: {input_file}")
        
        # Gerar nome do arquivo de saída se não fornecido
        if not output_file:
            base_name = os.path.splitext(input_file)[0]
            output_file = f"{base_name}_translated_{self.config.target_language}.csv"
        
        print(f"🔄 Iniciando tradução de: {input_file}")
        print(f"📄 Arquivo de saída: {output_file}")
        print(f"🌐 Traduzindo de {self.config.source_language} para {self.config.target_language}")
        
        try:
            with open(input_file, 'r', encoding='utf-8', newline='') as infile:
                # Detectar delimitador e configurações do CSV
                sample = infile.read(1024)
                infile.seek(0)
                sniffer = csv.Sniffer()
                delimiter = sniffer.sniff(sample).delimiter
                
                # Usar configurações que preservam aspas originais
                reader = csv.reader(infile, delimiter=delimiter, quotechar='"')
                rows = list(reader)
                
                with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
                    writer = csv.writer(outfile, delimiter=delimiter, quotechar='"', 
                                      quoting=csv.QUOTE_MINIMAL)
                    
                    # Escrever linha 1 (cabeçalho) - mantém original
                    if len(rows) > 0:
                        writer.writerow(rows[0])
                        print("📋 Linha 1 (cabeçalho): mantida original")
                    
                    # Escrever linha 2 (dados originais) - mantém original  
                    if len(rows) > 1:
                        writer.writerow(rows[1])
                        print("� Linha 2 (dados originais): mantida original")
                    
                    # Traduzir linha 2 para os idiomas solicitados e adicionar como linha 3+
                    if len(rows) > 1:
                        original_data_row = rows[1]
                        translated_cells = 0
                        
                        print(f"🔄 Traduzindo dados da linha 2 para {self.config.target_language}...")
                        
                        translated_row = []
                        for cell in original_data_row:
                            if cell and cell.strip():
                                translated_cell = self._translate_text(cell)
                                translated_row.append(translated_cell)
                                
                                if translated_cell != cell:
                                    translated_cells += 1
                            else:
                                translated_row.append(cell)
                        
                        # Escrever linha traduzida
                        writer.writerow(translated_row)
                        print(f"✅ Linha 3 ({self.config.target_language}): tradução adicionada")
                        
                        print(f"🔤 Células traduzidas: {translated_cells}")
                    
                    total_rows = len(rows) + 1 if len(rows) > 1 else len(rows)  # Original + 1 tradução
            
            print(f"✅ Tradução concluída!")
            print(f"📈 Total de linhas no arquivo final: {total_rows}")
            print(f"💾 Arquivo salvo em: {output_file}")
            
            return output_file
            
        except Exception as e:
            print(f"❌ Erro durante a tradução: {e}")
            raise

def create_config_file(filename: str = "translation_config.json"):
    """Cria um arquivo de configuração de exemplo"""
    config = {
        "source_language": "pt",
        "target_language": "en",
        "currency_symbol": "$",
        "convert_currency": False,
        "currency_conversion_rate": 5.5,
        "preserve_numbers": True,
        "preserve_urls": True,
        "preserve_emails": True,
        "max_retries": 3
    }
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    
    print(f"📋 Arquivo de configuração criado: {filename}")

def load_config_from_file(filename: str) -> TranslationConfig:
    """Carrega configuração de um arquivo JSON"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            config_dict = json.load(f)
        
        return TranslationConfig(**config_dict)
    except Exception as e:
        print(f"⚠️  Erro ao carregar configuração: {e}")
        return TranslationConfig()

def main():
    """Função principal do script"""
    parser = argparse.ArgumentParser(
        description="Tradutor CSV - Traduz textos em arquivos CSV mantendo formatação",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:

  # Tradução básica do português para inglês
  python tradutor_csv.py arquivo.csv

  # Especificar idiomas e arquivo de saída
  python tradutor_csv.py arquivo.csv -s pt -t es -o arquivo_espanhol.csv

  # Converter moedas com taxa específica
  python tradutor_csv.py arquivo.csv -t en --convert-currency --rate 5.5

  # Usar arquivo de configuração
  python tradutor_csv.py arquivo.csv --config config.json

  # Criar arquivo de configuração
  python tradutor_csv.py --create-config

Idiomas suportados: pt, en, es, fr, de, it, ja, zh, ko, ru, ar, hi
        """
    )
    
    parser.add_argument('input_file', nargs='?', help='Arquivo CSV de entrada')
    parser.add_argument('-o', '--output', help='Arquivo CSV de saída')
    parser.add_argument('-s', '--source', default='pt', help='Idioma de origem (padrão: pt)')
    parser.add_argument('-t', '--target', default='en', help='Idioma de destino (padrão: en)')
    parser.add_argument('--currency-symbol', default='$', help='Símbolo da moeda (padrão: $)')
    parser.add_argument('--convert-currency', action='store_true', help='Converter valores monetários')
    parser.add_argument('--rate', type=float, default=1.0, help='Taxa de conversão de moeda')
    parser.add_argument('--preserve-numbers', action='store_true', default=True, help='Preservar números')
    parser.add_argument('--config', help='Arquivo de configuração JSON')
    parser.add_argument('--create-config', action='store_true', help='Criar arquivo de configuração')
    
    args = parser.parse_args()
    
    # Criar arquivo de configuração se solicitado
    if args.create_config:
        create_config_file()
        return
    
    # Verificar se arquivo de entrada foi fornecido
    if not args.input_file:
        print("❌ Erro: Arquivo de entrada é obrigatório")
        parser.print_help()
        sys.exit(1)
    
    # Carregar configuração
    if args.config:
        config = load_config_from_file(args.config)
    else:
        config = TranslationConfig(
            source_language=args.source,
            target_language=args.target,
            currency_symbol=args.currency_symbol,
            convert_currency=args.convert_currency,
            currency_conversion_rate=args.rate,
            preserve_numbers=args.preserve_numbers
        )
    
    print("🚀 Tradutor CSV v1.0")
    print("=" * 50)
    
    # Verificar dependências
    if not GOOGLETRANS_AVAILABLE:
        print("❌ Google Translate não está disponível. Instale com:")
        print("pip install googletrans==4.0.0rc1")
        sys.exit(1)
    
    try:
        # Criar tradutor e executar
        translator = CSVTranslator(config)
        output_file = translator.translate_csv(args.input_file, args.output)
        
        print("\n🎉 Tradução concluída com sucesso!")
        print(f"📂 Arquivo traduzido salvo em: {output_file}")
        
    except Exception as e:
        print(f"\n❌ Erro durante a execução: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
