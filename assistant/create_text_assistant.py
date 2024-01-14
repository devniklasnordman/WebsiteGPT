import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client with your API key from environment variables
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Your uploaded file ID
uploaded_file_id = "file-xxx"  # Replace with your actual file ID

def create_text_based_assistant():
    """
    Function to create a text-based assistant with access to the .csv file in OpenAI.
    """
    try:
        assistant = client.beta.assistants.create(
            name="Text-Based Game Wizard",
            description="I am a text-based assistant that provides concise and informative responses based on video game sales data, with access to a .csv file for data retrieval.",
            model="gpt-4-1106-preview",  # Using GPT-4 model
            tools=[{"type": "code_interpreter"}, {"type": "retrieval"}],
            file_ids=[uploaded_file_id]  # Include the .csv file
            # Not including tools for text-only responses
        )
        return assistant.id
    except Exception as e:
        print(f"Error creating assistant: {e}")
        return None

# Create the assistant
assistant_id = create_text_based_assistant()
if assistant_id:
    print(f"Assistant created successfully. Assistant ID: {assistant_id}")
else:
    print("Failed to create assistant.")
