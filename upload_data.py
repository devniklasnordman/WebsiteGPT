import os
from openai import OpenAI
import pathlib
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client with your API key from environment variables
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def upload_file(file_path):
    """
    Function to upload a file to OpenAI for use with assistants.
    """
    try:
        with open(file_path, 'rb') as file:
            response = client.files.create(
                file=file,
                purpose='assistants',  # Use 'assistants' as the purpose
            )
        return response.id
    except Exception as e:
        print(f"Error uploading file: {e}")
        return None


# Path to your dataset file
file_path = pathlib.Path('csvjson.json')  # Replace with your actual CSV file name

# Upload the file and get the file ID
file_id = upload_file(file_path)
if file_id:
    print(f"File uploaded successfully. File ID: {file_id}")
else:
    print("Failed to upload the file.")
