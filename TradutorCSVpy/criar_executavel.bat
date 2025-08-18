@echo off
chcp 65001 >nul 2>&1
echo.
echo ████████╗██████╗  █████╗ ██████╗ ██╗   ██╗███████╗ █████╗ ██╗
echo ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║   ██║╚══███╔╝██╔══██╗██║
echo    ██║   ██████╔╝███████║██║  ██║██║   ██║  ███╔╝ ███████║██║
echo    ██║   ██╔══██╗██╔══██║██║  ██║██║   ██║ ███╔╝  ██╔══██║██║
echo    ██║   ██║  ██║██║  ██║██████╔╝╚██████╔╝███████╗██║  ██║██║
echo    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝
echo.
echo                    🌍 CSV TRANSLATOR 🌍
echo                 Criador de Executável v1.0
echo                   by Wedny Fernandes
echo.
echo ================================================================
echo.

REM Verificar se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python não encontrado!
    echo 💡 Instale Python 3.7+ em https://python.org
    pause
    exit /b 1
)

echo ✅ Python encontrado
echo.

REM Verificar se o arquivo principal existe
if not exist "tradutor_csv_gui.py" (
    echo ❌ Arquivo tradutor_csv_gui.py não encontrado!
    echo 💡 Certifique-se de estar na pasta correta
    pause
    exit /b 1
)

echo ✅ Arquivo principal encontrado
echo.

REM Instalar dependências se necessário
echo 📦 Verificando dependências...
python -c "import googletrans" >nul 2>&1
if errorlevel 1 (
    echo 📥 Instalando googletrans...
    pip install googletrans==4.0.0rc1
)

python -c "import PyInstaller" >nul 2>&1
if errorlevel 1 (
    echo 📥 Instalando PyInstaller...
    pip install pyinstaller
)

echo ✅ Dependências verificadas
echo.

REM Limpar builds anteriores
if exist "build" (
    echo 🧹 Limpando build anterior...
    rmdir /s /q "build"
)

if exist "dist" (
    echo 🧹 Limpando dist anterior...
    rmdir /s /q "dist"
)

if exist "*.spec" (
    echo 🧹 Limpando arquivos spec...
    del /q "*.spec"
)

echo.
echo 🔨 Criando executável...
echo ⏳ Isso pode levar alguns minutos...
echo.

REM Criar executável
pyinstaller --onefile --windowed --name=TraduzAI-CSV --hidden-import=googletrans --hidden-import=tkinter --clean tradutor_csv_gui.py

if errorlevel 1 (
    echo.
    echo ❌ Erro ao criar executável!
    echo 💡 Verifique as mensagens de erro acima
    pause
    exit /b 1
)

echo.
echo ✅ Executável criado com sucesso!
echo.
echo 📁 Localização: %CD%\dist\TraduzAI-CSV.exe
echo 📏 Tamanho: 
for %%I in ("dist\TraduzAI-CSV.exe") do echo    %%~zI bytes

echo.
echo 🎉 PROCESSO CONCLUÍDO!
echo.
echo 💡 Informações importantes:
echo    • O executável está na pasta 'dist'
echo    • Pode ser distribuído independentemente
echo    • Não requer Python no computador de destino
echo    • Funciona no Windows 7, 8, 10 e 11
echo.

REM Oferecer para abrir a pasta
set /p open_folder="🚀 Deseja abrir a pasta dist? (s/n): "
if /i "%open_folder%"=="s" (
    start "" "dist"
)

echo.
echo 📋 Para testar:
echo    1. Vá para a pasta dist
echo    2. Execute TraduzAI-CSV.exe
echo    3. Selecione um arquivo CSV
echo    4. Configure os idiomas
echo    5. Clique em 'Iniciar Tradução'
echo.

pause
