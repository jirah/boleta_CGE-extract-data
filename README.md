# boleta_CGE-extract-data
Extrae data (monto a pagar y kWh consumidos) de la boleta de CGE para cálculos básicos de consumo


# Instalacion de las librerias
pip install pymupdf pandas ace-tools

# Para confirmar que las librerias se instalaron correctamente
python3 -c "import fitz, pandas, PIL, ace-tools; print('Todo funciona correctamente')"

# Para correr el script
python3 Boletas_CGE_Data_Extraction.py
