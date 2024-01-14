import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client with your API key from environment variables
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Your uploaded file ID
uploaded_file_id = "file-xxx"  # Replace with your actual file ID

def create_assistant():
    """
    Function to create an assistant in OpenAI.
    """
    try:
        assistant = client.beta.assistants.create(
            name="Data Visualizer",
            description="You are great at creating beautiful data visualizations. You analyze data present in .csv files, understand trends, and come up with data visualizations relevant to those trends. You also share a brief text summary of the trends observed.",
            model="gpt-4-1106-preview",  # Ensure this model is compatible with the tools you want to use
            tools=[{"type": "code_interpreter"}],
            file_ids=[uploaded_file_id]
        )
        return assistant.id
    except Exception as e:
        print(f"Error creating assistant: {e}")
        return None

# Create the assistant
assistant_id = create_assistant()
if assistant_id:
    print(f"Assistant created successfully. Assistant ID: {assistant_id}")
else:
    print("Failed to create assistant.")
