from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv
import os
import time

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY')) # Store your api-key in .env file

# Your prebuilt assistant's ID
assistant_id = os.getenv('ASSISTANT_ID')  # Store your assistant ID in .env file

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({"response": "No prompt provided"}), 400

    try:
        print("Creating thread...")
        thread = client.beta.threads.create()

        print(f"Adding message to thread {thread.id}...")
        client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=prompt
        )

        print(f"Running the assistant on thread {thread.id}...")
        client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant_id
        )

        print(f"Waiting for the assistant's response...")
        time.sleep(5)  # Increased delay to ensure response time

        print(f"Retrieving messages from thread {thread.id}...")
        messages = client.beta.threads.messages.list(thread_id=thread.id)

        response_text = "No response from assistant."
        for msg in messages.data:
            print(f"Message ID: {msg.id}, Role: {msg.role}, Content: {msg.content[0].text.value}")
            if msg.role == "assistant":
                response_text = msg.content[0].text.value

        print(f"Final Response: {response_text}")
        return jsonify({"response": response_text})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"response": "Error processing your request"}), 3000

if __name__ == '__main__':
    app.run(port=5001)