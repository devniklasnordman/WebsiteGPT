WebsiteGPT
Frontend Initialization:
Client Environment Variables:
Create a file called .env in the root of the 'client' folder.

Add the following line to the .env file (without extra spaces or other symbols):

arduino
Copy code
REACT_APP_BACKEND_URL=http://localhost:3001
Starting the Client:
Change the directory location to WebsiteGPT\client.

In the terminal, run the following command:

sql
Copy code
npm start
Backend Initialization:
Server Environment Variables:
Create a file called .env in the root of the 'server' folder.

Add the following lines to the .env file (without extra spaces or other symbols):

makefile
Copy code
OPENAI_API_KEY=<your_openai_api_key>
PORT=3001
Starting the Server:
Change the directory location to WebsiteGPT\server.

In the terminal, run the following command:

Copy code
node app.js
Setting up the OpenAI Assistant:
Create your own assistant at OpenAI Assistants.

This version is powered by the gpt-3.5-turbo-1106 model.

Note: The gpt-4 model is expensive to use due to its token consumption.

In the OpenAI assistant configuration page, remember to enable the following tools for the assistant:

Retrieval
Code interpreter
Get your OpenAI API key from OpenAI API Keys.

Keep your API key safe as it is displayed only once.
Setting up the Python assistant_service:
Create a file called .env in the root of the project folder.

Add the following lines to the .env file (without extra spaces or other symbols):

makefile
Copy code
OPENAI_API_KEY=<your_openai_api_key>
ASSISTANT_ID=<your_assistant_id>
Run the assistant_service.py file.

Dataset Information:
The dataset is sourced from Global Video Game Sales and Reviews by Andy Bramwell.

The data has been converted to JSON format and attached to the assistant.

The JSON data is included in the root of the Python project as csvjson.json in case you want to use it with your assistant.
Prototype Features:
This prototype can answer simple questions based on the dataset, such as:

"What is the rank 1 game globally?"
"What is the most popular Pokémon game?"
For more complex analytical questions that require multiple queries to the dataset, the assistant may provide several responses before delivering the final answer.

Please note that the frontend does not support or render complex questions, but you can test the assistant at the OpenAI Playground.

Relevant Documentation:
OpenAI Python API Library

v1.0.0 Migration Guide #742

OpenAI Assistants

This reformatted README should make it easier for readers to understand the steps and information provided in your project documentation. Feel free to further customize it as needed.
