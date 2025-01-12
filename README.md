# Unicode Range Extractor for TMP Fonts in Unity

This tool extracts unique Unicode characters from a specified column in an Excel file and generates two output files:

1. A **readable list** of unique characters, their indices, and Unicode values.
2. A **Unicode range string** suitable for creating custom TMP (TextMeshPro) fonts in Unity with only the required characters.

## Features

- Reads text data from a specified column in an Excel file.
- Identifies all unique characters used in the text.
- Outputs a human-readable list of characters and their Unicode values.
- Generates a Unicode range string in the format required for Unity TMP font generation.

## Requirements

- Python 3.7 or higher
- `pandas` library
- `openpyxl` library (for reading Excel files)

Install the required dependencies using:

```bash
pip install pandas openpyxl
