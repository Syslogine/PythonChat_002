# ChatBot Script Tutorial

This tutorial provides a breakdown of the Python script for a ChatBot using the OpenAI GPT-3.5 Turbo model. The script allows users to interact with the ChatBot, with the option to exit the conversation, view chat history, and receive assistance.

## Prerequisites
Before using the script, make sure to set up your OpenAI API key. You need to create a `config.py` file with your API key. Example content:

```python
# config.py

OPENAI_API_KEY = "your-api-key"
OPENAI_MODEL_NAME = "gpt-3.5-turbo"
EXIT_COMMAND = "stop chat"
OPENAI_API_ENDPOINT = "https://api.openai.com/v1/"

if not OPENAI_API_KEY:
    raise ValueError("Please provide a valid OpenAI API key.")
```

## Script Overview

### 1. Import Libraries and Modules
```python
import json
import logging
import requests
from os import path
from config import EXIT_COMMAND, OPENAI_API_KEY, OPENAI_MODEL_NAME, OPENAI_API_ENDPOINT
from openai import OpenAI, OpenAIError
```

### 2. Initialize OpenAI Client
```python
api_key = OPENAI_API_KEY
client = OpenAI(api_key=api_key)
```

### 3. Define Functions

#### a. `chat_with_openai(prompt, history)`
Handles the conversation with OpenAI GPT-3.5 Turbo.
- Appends user input to the conversation history.
- Sends a request to OpenAI's chat completions endpoint.
- Handles API errors and returns AI responses.

#### b. `save_chat_history(history, filename="chat_history.json")`
Saves the chat history to a JSON file.

#### c. `show_help()`
Displays a help message with usage instructions.

#### d. `show_chat_history(history, max_display=5)`
Displays the recent chat history.

#### e. `load_chat_history(filename="chat_history.json")`
Loads the chat history from a JSON file.

### 4. Main Execution in `main()`

- Loads existing chat history.
- Initiates a conversation loop.
- Handles user input, including exit command, help, and history display.
- Uses OpenAI for user input and displays AI responses.
- Saves the updated chat history.

### 5. Run the Script
```python
if __name__ == "__main__":
    main()
```

## How to Use

1. Run the script.
2. Enter your messages as a user.
3. Type 'exit' to end the conversation.
4. Type 'help' for assistance.
5. Type 'history' to view recent chat history.

