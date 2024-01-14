import pandas as pd

def csv_to_json(csv_file_path, json_file_path, csv_encoding='utf-8'):
    try:
        # Read the CSV file using Pandas with specified encoding
        df = pd.read_csv(csv_file_path, encoding=csv_encoding)

        # Convert the DataFrame to JSON format
        json_data = df.to_json(orient='records', lines=True)

        # Write the JSON data to a file with UTF-8 encoding
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json_file.write(json_data)

        print("Conversion successful!")
    except Exception as e:
        print(f"Error during conversion: {e}")

# Example usage
csv_file_path = ''  # Replace with your CSV file path
json_file_path = 'gamedata.json'  # Replace with your desired JSON file path

# Try with different encodings if UTF-8 doesn't work, e.g., 'ISO-8859-1'
csv_to_json(csv_file_path, json_file_path, csv_encoding='utf-8')

game_sales.csv
gamedata.json