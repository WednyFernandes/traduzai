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
    
    # Testar configuração com BooleanVar (como no executável)
    import tkinter as tk
    root = tk.Tk()
    root.withdraw()
    
    app = CSVTranslatorGUI(root)
    
    # Simular valores nas variáveis BooleanVar
    app.preserve_numbers.set(True)
    app.preserve_urls.set(True) 
    app.preserve_emails.set(True)
    app.convert_currency.set(False)
    app.currency_symbol.set("$")
    app.currency_rate.set(1.0)
    app.source_lang.set("pt - Portuguese")
    app.target_lang.set("en - English")
    
    # Criar config como no método translate_csv
    config = TranslationConfig(
        source_language=app.source_lang.get().split(' - ')[0] if ' - ' in app.source_lang.get() else app.source_lang.get(),
        target_language=app.target_lang.get().split(' - ')[0] if ' - ' in app.target_lang.get() else app.target_lang.get(),
        currency_symbol=app.currency_symbol.get(),
        convert_currency=app.convert_currency.get(),
        currency_conversion_rate=app.currency_rate.get(),
        preserve_numbers=app.preserve_numbers.get(),
        preserve_urls=app.preserve_urls.get(),
        preserve_emails=app.preserve_emails.get()
    )
    
    print("✅ Configuração criada com sucesso!")
    print(f"   preserve_numbers: {config.preserve_numbers} (type: {type(config.preserve_numbers)})")
    print(f"   preserve_urls: {config.preserve_urls} (type: {type(config.preserve_urls)})")
    print(f"   preserve_emails: {config.preserve_emails} (type: {type(config.preserve_emails)})")
    
    # Testar texto que causou erro
    test_text = "Mendoza/Argentina \nLeve, com notas de frutas tropicais: abacaxi e maracujá"
    print(f"\n🧪 Testando texto problemático: {repr(test_text)}")
    
    # Testar funções individuais
    case_pattern = app.detect_case_pattern(test_text)
    print(f"✅ Padrão de caixa detectado: {case_pattern}")
    
    # Testar preservação de elementos
    preserved_text, placeholders = app.preserve_elements(test_text, config)
    print(f"✅ Texto preservado: {repr(preserved_text)}")
    print(f"✅ Placeholders: {placeholders}")
    
    restored_text = app.restore_elements(preserved_text, placeholders)
    print(f"✅ Texto restaurado: {repr(restored_text)}")
    
    # Testar com texto em maiúsculas também
    test_text2 = "SOL SUL TORRENTÉS"
    print(f"\n🧪 Testando texto em maiúsculas: {repr(test_text2)}")
    
    case_pattern2 = app.detect_case_pattern(test_text2)
    print(f"✅ Padrão de caixa detectado: {case_pattern2}")
    
    preserved_text2, placeholders2 = app.preserve_elements(test_text2, config)
    print(f"✅ Texto preservado: {repr(preserved_text2)}")
    
    restored_text2 = app.restore_elements(preserved_text2, placeholders2)
    print(f"✅ Texto restaurado: {repr(restored_text2)}")
    
    root.destroy()
    
    print("\n🎉 Todos os testes passaram! O erro foi corrigido.")
    
except Exception as e:
    print(f"❌ Erro durante o teste: {e}")
    import traceback
    traceback.print_exc()
