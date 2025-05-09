# Required Libraries
import os
import re
import fitz  # PyMuPDF
import pandas as pd
import ace_tools as tools

# Path to the extracted PDF files
pdf_folder_path = '/home/data/Boletas_CGE/'

# Prepare lists to store extracted data
months = []
total_to_pay_list = []
electricity_consumed_list = []

total_to_pay_pattern = r"Total a pagar\s*\$\s*([\d\.,]+)"
electricity_consumed_pattern = r"Electricidad consumida.*?\((\d+\s?kWh)\)"

# Process each PDF file
pdf_files = [f for f in os.listdir(pdf_folder_path) if f.endswith('.pdf')]
for pdf_file in pdf_files:
    file_path = os.path.join(pdf_folder_path, pdf_file)
    combined_text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            blocks = page.get_text("blocks")
            for block in blocks:
                # Combine meaningful text blocks
                if block[4].strip():
                    combined_text += block[4].replace("\n", " ").strip() + "\n"
    
    # Extract total to pay
    total_match = re.search(total_to_pay_pattern, combined_text, re.DOTALL)
    total_to_pay = total_match.group(1).replace('.', '').replace(',', '.').strip() if total_match else "Not Found"
    total_to_pay_list.append(total_to_pay)

    # Extract electricity consumed
    consumed_match = re.search(electricity_consumed_pattern, combined_text, re.DOTALL)
    electricity_consumed = consumed_match.group(1).replace(' kWh', '').strip() if consumed_match else "Not Found"
    electricity_consumed_list.append(electricity_consumed)

    # Extract the month from the filename
    month = pdf_file.replace('.pdf', '')
    months.append(month)

# Create the DataFrame
data_df = pd.DataFrame({
    "Month": months,
    "Total a Pagar (CLP)": total_to_pay_list,
    "Electricidad Consumida (kWh)": electricity_consumed_list
})

tools.display_dataframe_to_user("Boletas CGE Data Final Corrected", data_df)