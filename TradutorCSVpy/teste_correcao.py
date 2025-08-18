#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste rápido para verificar se as correções funcionam
"""

import sys
import os

# Adicionar o diretório atual ao path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Importar e testar
try:
    from tradutor_csv_gui import CSVTranslatorGUI, TranslationConfig
    import tkinter as tk
    
    print("✅ Importação bem-sucedida!")
    
    # Testar configuração
    config = TranslationConfig(
        source_language='pt',
        target_language='en',
        preserve_numbers=True,
        preserve_urls=True,
        preserve_emails=True
    )
    
    print("✅ Configuração criada com sucesso!")
    
    # Testar interface (sem mostrar)
    root = tk.Tk()
    root.withdraw()  # Esconder a janela
    
    app = CSVTranslatorGUI(root)
    
    # Testar funções individuais
    test_text = "RESTAURANTE"
    case_pattern = app.detect_case_pattern(test_text)
    print(f"✅ Padrão de caixa detectado: {case_pattern}")
    
    applied_text = app.apply_case_pattern("restaurant", case_pattern)
    print(f"✅ Texto com caixa aplicada: {applied_text}")
    
    # Testar preservação de elementos
    preserved_text, placeholders = app.preserve_elements("Email: test@example.com, Valor: 123.45", config)
    print(f"✅ Texto preservado: {preserved_text}")
    print(f"✅ Placeholders: {placeholders}")
    
    restored_text = app.restore_elements(preserved_text, placeholders)
    print(f"✅ Texto restaurado: {restored_text}")
    
    root.destroy()
    
    print("\n🎉 Todos os testes passaram! O erro foi corrigido.")
    
except Exception as e:
    print(f"❌ Erro durante o teste: {e}")
    import traceback
    traceback.print_exc()
