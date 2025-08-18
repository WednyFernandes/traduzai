#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para criar executável do TraduzAI CSV
Autor: Wedny Fernandes
Data: 2025-08-17
"""

import subprocess
import sys
import os

def install_pyinstaller():
    """Instala PyInstaller se não estiver disponível"""
    try:
        import PyInstaller
        print("✅ PyInstaller já está instalado")
    except ImportError:
        print("📦 Instalando PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✅ PyInstaller instalado com sucesso")

def create_executable():
    """Cria o executável"""
    print("🔨 Criando executável...")
    
    # Comando PyInstaller
    cmd = [
        "pyinstaller",
        "--onefile",                    # Arquivo único
        "--windowed",                   # Sem console (GUI)
        "--name=TraduzAI-CSV",         # Nome do executável
        "--icon=icon.ico",             # Ícone (se disponível)
        "--add-data=translation_config.json;.",  # Incluir arquivo de config
        "--hidden-import=googletrans", # Importação hidden
        "--hidden-import=tkinter",     # Importação hidden
        "tradutor_csv_gui.py"          # Arquivo principal
    ]
    
    # Remover ícone se não existir
    if not os.path.exists("icon.ico"):
        cmd.remove("--icon=icon.ico")
    
    # Remover config se não existir
    if not os.path.exists("translation_config.json"):
        cmd.remove("--add-data=translation_config.json;.")
    
    try:
        subprocess.run(cmd, check=True)
        print("✅ Executável criado com sucesso!")
        print("📁 Verifique a pasta 'dist' para o arquivo TraduzAI-CSV.exe")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao criar executável: {e}")
        return False
    
    return True

def main():
    print("🚀 TraduzAI CSV - Gerador de Executável")
    print("=" * 50)
    
    # Verificar se o arquivo principal existe
    if not os.path.exists("tradutor_csv_gui.py"):
        print("❌ Arquivo tradutor_csv_gui.py não encontrado!")
        return
    
    # Instalar PyInstaller
    install_pyinstaller()
    
    # Criar executável
    if create_executable():
        print("\n🎉 Processo concluído!")
        print("💡 Dicas:")
        print("   - O executável está na pasta 'dist'")
        print("   - Pode ser distribuído independentemente")
        print("   - Não requer Python instalado no computador de destino")
    else:
        print("\n❌ Falha ao criar executável")

if __name__ == "__main__":
    main()
