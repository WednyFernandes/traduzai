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
import shutil
from pathlib import Path

def install_pyinstaller():
    """Instala PyInstaller se não estiver disponível"""
    try:
        import PyInstaller
        print("✅ PyInstaller já está instalado")
    except ImportError:
        print("📦 Instalando PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✅ PyInstaller instalado com sucesso")

def create_temp_directory():
    """Cria diretório temporário em local sem espaços"""
    # Tentar primeiro C:\temp, depois área de trabalho
    possible_locations = [
        Path("C:/temp/TraduzAI-Build"),
        Path("C:/TraduzAI-Build"),
        Path.home() / "Desktop" / "TraduzAI-Build"
    ]
    
    for temp_dir in possible_locations:
        try:
            # Verificar se o diretório pai existe e é acessível
            if temp_dir.parent.exists() or temp_dir.parent == Path("C:/"):
                # Limpar se existir
                if temp_dir.exists():
                    print(f"🧹 Limpando pasta anterior: {temp_dir}")
                    shutil.rmtree(temp_dir)
                
                # Criar nova pasta
                temp_dir.mkdir(parents=True, exist_ok=True)
                print(f"📁 Pasta temporária criada: {temp_dir}")
                
                # Testar se podemos escrever
                test_file = temp_dir / "test.txt"
                test_file.write_text("test")
                test_file.unlink()
                
                return temp_dir
                
        except Exception as e:
            print(f"⚠️ Erro ao criar {temp_dir}: {e}")
            continue
    
    raise RuntimeError("Não foi possível criar pasta temporária em nenhum local")

def copy_files_to_temp(temp_dir):
    """Copia arquivos necessários para pasta temporária"""
    current_dir = Path(__file__).parent
    
    # Arquivos obrigatórios
    required_files = ["tradutor_csv_gui.py"]
    
    # Arquivos opcionais
    optional_files = ["translation_config.json", "icon.ico"]
    
    print("📋 Copiando arquivos...")
    
    for file in required_files:
        src = current_dir / file
        if src.exists():
            shutil.copy2(src, temp_dir)
            print(f"  ✅ {file}")
        else:
            print(f"  ❌ {file} não encontrado!")
            return False
    
    for file in optional_files:
        src = current_dir / file
        if src.exists():
            shutil.copy2(src, temp_dir)
            print(f"  ✅ {file}")
        else:
            print(f"  ⚠️ {file} não encontrado (opcional)")
    
    return True

def create_executable(temp_dir):
    """Cria o executável"""
    print("🔨 Criando executável...")
    print("⏳ Isso pode levar alguns minutos...")
    
    # Mudar para diretório temporário
    original_dir = os.getcwd()
    
    try:
        os.chdir(str(temp_dir))  # Converter Path para string
        
        # Comando PyInstaller - versão simplificada para evitar problemas
        cmd = [
            "pyinstaller",
            "--onefile",                    # Arquivo único
            "--windowed",                   # Sem console (GUI)
            "--name=TraduzAI-CSV",         # Nome do executável
            "--hidden-import=googletrans", # Importação hidden
            "--hidden-import=tkinter",     # Importação hidden
            "--clean",                     # Limpeza
            "--distpath=./dist",           # Pasta de destino
            "--workpath=./build",          # Pasta de trabalho
            "tradutor_csv_gui.py"          # Arquivo principal
        ]
        
        # Executar PyInstaller
        print("🔧 Executando PyInstaller...")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Executável criado com sucesso!")
            return True
        else:
            print(f"❌ Erro ao criar executável (código: {result.returncode})")
            print("Saída do erro:")
            print(result.stderr)
            print("Saída padrão:")
            print(result.stdout)
            return False
        
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False
    
    finally:
        # Voltar ao diretório original
        os.chdir(original_dir)

def copy_executable_to_desktop(temp_dir):
    """Copia executável para área de trabalho"""
    exe_path = temp_dir / "dist" / "TraduzAI-CSV.exe"
    desktop = Path.home() / "Desktop"
    
    if exe_path.exists():
        shutil.copy2(exe_path, desktop)
        print(f"📋 Executável copiado para: {desktop / 'TraduzAI-CSV.exe'}")
        
        # Mostrar tamanho
        size = exe_path.stat().st_size
        size_mb = size / (1024 * 1024)
        print(f"📏 Tamanho: {size_mb:.1f} MB ({size:,} bytes)")
        
        return desktop / "TraduzAI-CSV.exe"
    else:
        print(f"❌ Executável não encontrado em: {exe_path}")
        return None

def cleanup_temp_directory(temp_dir):
    """Remove diretório temporário"""
    try:
        shutil.rmtree(temp_dir)
        print("✅ Pasta temporária removida")
    except Exception as e:
        print(f"⚠️ Erro ao remover pasta temporária: {e}")

def main():
    print("🚀 TraduzAI CSV - Gerador de Executável")
    print("=" * 50)
    
    # Verificar se o arquivo principal existe
    current_dir = Path(__file__).parent
    main_file = current_dir / "tradutor_csv_gui.py"
    
    if not main_file.exists():
        print("❌ Arquivo tradutor_csv_gui.py não encontrado!")
        print(f"   Procurado em: {main_file}")
        input("Pressione Enter para sair...")
        return
    
    try:
        # Instalar PyInstaller
        install_pyinstaller()
        
        # Criar diretório temporário
        temp_dir = create_temp_directory()
        
        # Copiar arquivos
        if not copy_files_to_temp(temp_dir):
            print("❌ Falha ao copiar arquivos necessários")
            return
        
        # Criar executável
        if not create_executable(temp_dir):
            print("❌ Falha ao criar executável")
            return
        
        # Copiar executável para área de trabalho
        exe_path = copy_executable_to_desktop(temp_dir)
        
        if exe_path:
            print("\n🎉 PROCESSO CONCLUÍDO!")
            print("💡 Dicas:")
            print(f"   - O executável está na área de trabalho: {exe_path.name}")
            print("   - Pode ser distribuído independentemente")
            print("   - Não requer Python instalado no computador de destino")
            print("   - Funciona no Windows 7, 8, 10 e 11")
            
            # Perguntar se quer abrir área de trabalho
            response = input("\n🚀 Deseja abrir a área de trabalho? (s/n): ").strip().lower()
            if response in ['s', 'sim', 'y', 'yes']:
                import webbrowser
                webbrowser.open(str(Path.home() / "Desktop"))
        
        # Perguntar se quer limpar pasta temporária
        response = input("🧹 Deseja limpar pasta temporária? (s/n): ").strip().lower()
        if response in ['s', 'sim', 'y', 'yes']:
            cleanup_temp_directory(temp_dir)
        
    except KeyboardInterrupt:
        print("\n⏹️ Processo cancelado pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        import traceback
        traceback.print_exc()
    
    input("\nPressione Enter para sair...")

if __name__ == "__main__":
    main()
