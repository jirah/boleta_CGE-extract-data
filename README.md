# boleta_CGE-extract-data
Extrae data (monto a pagar y kWh consumidos) de la boleta de CGE para cálculos básicos de consumo

# Instalacion de las librerias
pip install pymupdf pandas ace-tools

# Para confirmar que las librerias se instalaron correctamente
python3 -c "import fitz, pandas, PIL, ace-tools; print('Todo funciona correctamente')"

# Para correr el script
python3 CGE-extract_data.py

# Los resultados se van a ver asi, en un archivo CSV que puedes abrir en Excel o similares:
![image](https://github.com/user-attachments/assets/8dbcd04b-ce05-418e-91c4-1c9f0da8f50d)
