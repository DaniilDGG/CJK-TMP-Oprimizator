import pandas as pd

def extract_unique_characters(file_path, column_name, readable_output_file, tmp_output_file):
    data = pd.read_excel(file_path)

    if column_name not in data.columns:
        print(f"Column '{column_name}' not found in the table.")
        return

    column_data = data[column_name].dropna()

    # Combine all text from the column
    text = " ".join(column_data.values)

    # Extract unique characters 
    unique_characters = sorted(list(set(text)))

    # Write to readable output file
    with open(readable_output_file + ".txt", 'w', encoding='utf-8') as file:
        for char in unique_characters:
            file.write(f"{char}: {ord(char):x}\n")

    # Write to TMP output file
    with open(tmp_output_file + ".txt", 'w', encoding='utf-8') as file:
        for char in unique_characters:
            file.write(f"\\u{ord(char):x}")

    print("Unique characters saved to", readable_output_file + ".txt", "and", tmp_output_file + ".txt")

file_path = input("Enter the path to the Excel file: ")
column_name = input("Enter the column name: ")
readable_output_file = input("Enter the readable output file name: ")
tmp_output_file = input("Enter the TMP output file name: ")

extract_unique_characters(file_path, column_name, readable_output_file, tmp_output_file)