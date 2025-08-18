@echo off
cls
echo.
echo =========================================================
echo           DEMONSTRAÇÃO DO TRADUTOR CSV
echo =========================================================
echo.
echo Este script demonstra diferentes funcionalidades:
echo.
echo 1. Tradução básica (PT → EN) com símbolo de moeda
echo 2. Tradução com conversão de moeda
echo 3. Tradução para espanhol
echo 4. Uso de arquivo de configuração
echo.
pause

echo.
echo [1/4] Tradução básica para inglês...
python tradutor_csv.py teste_pequeno.csv -t en --currency-symbol "$" -o demo_basic_en.csv
echo ✅ Concluído: demo_basic_en.csv
echo.

echo [2/4] Tradução com conversão de moeda (1 Real = 0.18 USD)...
python tradutor_csv.py teste_pequeno.csv -t en --convert-currency --rate 0.18 --currency-symbol "$" -o demo_converted_en.csv
echo ✅ Concluído: demo_converted_en.csv
echo.

echo [3/4] Tradução para espanhol...
python tradutor_csv.py teste_pequeno.csv -t es --currency-symbol "€" -o demo_es.csv
echo ✅ Concluído: demo_es.csv
echo.

echo [4/4] Criando e usando configuração personalizada...
echo {> config_demo.json
echo   "source_language": "pt",>> config_demo.json
echo   "target_language": "fr",>> config_demo.json
echo   "currency_symbol": "€",>> config_demo.json
echo   "convert_currency": false,>> config_demo.json
echo   "preserve_numbers": true>> config_demo.json
echo }>> config_demo.json

python tradutor_csv.py teste_pequeno.csv --config config_demo.json -o demo_fr.csv
echo ✅ Concluído: demo_fr.csv
echo.

echo =========================================================
echo                    DEMONSTRAÇÃO CONCLUÍDA
echo =========================================================
echo.
echo Arquivos criados:
echo • demo_basic_en.csv      - Tradução básica inglês
echo • demo_converted_en.csv  - Tradução com conversão de moeda
echo • demo_es.csv           - Tradução espanhol
echo • demo_fr.csv           - Tradução francês com config
echo • config_demo.json      - Exemplo de configuração
echo.
echo Você pode abrir estes arquivos para ver os resultados!
echo.
pause
