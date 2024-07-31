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

    # Write readable output
    with open(readable_output_file + ".txt", 'w', encoding='utf-8') as file:
        for index, char in enumerate(unique_characters):
            file.write(f"{index}: {char} (U+{ord(char):04X})\n")

    code_points = [ord(char) for char in unique_characters]
    code_points.sort()

    def get_ranges(points):
        ranges = []
        start = end = points[0]
        for point in points[1:]:
            if point == end + 1:
                end = point
            else:
                if start == end:
                    ranges.append(f"{start:X}")
                else:
                    ranges.append(f"{start:X}-{end:X}")
                start = end = point
        if start == end:
            ranges.append(f"{start:X}")
        else:
            ranges.append(f"{start:X}-{end:X}")
        return ranges

    ranges = get_ranges(code_points)

    # Write TMP output
    with open(tmp_output_file + ".txt", 'w', encoding='utf-8') as file:
        file.write(",".join(ranges))

    print("Unique characters saved to", readable_output_file + ".txt", "and", tmp_output_file + ".txt")

# Enter the path to the Excel file, column name, and output file names
file_path = input("Enter the path to the Excel file: ")
column_name = input("Enter the column name: ")
readable_output_file = input("Enter the readable output file name: ")
tmp_output_file = input("Enter the TMP output file name: ")

extract_unique_characters(file_path, column_name, readable_output_file, tmp_output_file)