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

REM Criar pasta temporária na área de trabalho
set "TEMP_DIR=%USERPROFILE%\Desktop\TraduzAI-Build"
echo 📁 Criando pasta temporária: %TEMP_DIR%

if exist "%TEMP_DIR%" (
    echo 🧹 Limpando pasta anterior...
    rmdir /s /q "%TEMP_DIR%"
)

mkdir "%TEMP_DIR%"

REM Copiar arquivo necessário para pasta temporária
echo 📋 Copiando arquivos...
copy "tradutor_csv_gui.py" "%TEMP_DIR%\"
if exist "translation_config.json" copy "translation_config.json" "%TEMP_DIR%\"

REM Entrar na pasta temporária
cd /d "%TEMP_DIR%"

echo.
echo 🔨 Criando executável...
echo ⏳ Isso pode levar alguns minutos...
echo.

REM Criar executável na pasta temporária
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
echo 📁 Localização: %TEMP_DIR%\dist\TraduzAI-CSV.exe
echo 📏 Tamanho: 
for %%I in ("%TEMP_DIR%\dist\TraduzAI-CSV.exe") do echo    %%~zI bytes

REM Copiar executável para área de trabalho
echo.
echo 📋 Copiando executável para área de trabalho...
copy "%TEMP_DIR%\dist\TraduzAI-CSV.exe" "%USERPROFILE%\Desktop\"

echo.
echo 🎉 PROCESSO CONCLUÍDO!
echo.
echo 💡 Informações importantes:
echo    • O executável está na área de trabalho
echo    • Arquivo: TraduzAI-CSV.exe
echo    • Pode ser distribuído independentemente
echo    • Não requer Python no computador de destino
echo    • Funciona no Windows 7, 8, 10 e 11
echo.

REM Oferecer para abrir a área de trabalho
set /p open_desktop="🚀 Deseja abrir a área de trabalho? (s/n): "
if /i "%open_desktop%"=="s" (
    start "" "%USERPROFILE%\Desktop"
)

echo.
echo 📋 Para testar:
echo    1. Vá para a área de trabalho
echo    2. Execute TraduzAI-CSV.exe
echo    3. Selecione um arquivo CSV
echo    4. Configure os idiomas
echo    5. Clique em 'Iniciar Tradução'
echo.

REM Limpar pasta temporária (opcional)
set /p clean_temp="🧹 Deseja limpar pasta temporária? (s/n): "
if /i "%clean_temp%"=="s" (
    cd /d "%USERPROFILE%"
    rmdir /s /q "%TEMP_DIR%"
    echo ✅ Pasta temporária limpa
)

pause
