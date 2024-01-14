import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client with your API key from environment variables
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def ask_question(question):
    """
    Function to send a question to the OpenAI Chat and get a response.
    """
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": question}],
            model="gpt-3.5-turbo"
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        print(f"Error in chat completion: {e}")
        return None

# Example usage
if __name__ == "__main__":
    response = ask_question("What are the top 3 action games in each region for the year 2005?")
    if response:
        print(response)
    else:
        print("No response received.")
