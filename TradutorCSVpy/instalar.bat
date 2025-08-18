@echo off
echo Instalando dependencias do Tradutor CSV...
echo.

REM Verificar se Python esta instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERRO: Python nao esta instalado ou nao esta no PATH
    echo Por favor, instale Python 3.7+ de https://python.org
    pause
    exit /b 1
)

REM Instalar dependencias
echo Instalando googletrans...
pip install googletrans==4.0.0rc1

if %errorlevel% neq 0 (
    echo.
    echo ERRO: Falha na instalacao das dependencias
    echo Tente executar como administrador
    pause
    exit /b 1
)

echo.
echo ✅ Instalacao concluida com sucesso!
echo.
echo Para usar o script:
echo python tradutor_csv.py seu_arquivo.csv
echo.
pause
