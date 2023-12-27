# PythonChat_002

This script, named PythonChat_002, interacts with the OpenAI GPT-3.5-turbo model to simulate a chat conversation between a user and an AI assistant.

## Usage

1. Replace the placeholder in `config.py` with your OpenAI API key:

   ```python
   # config.py
   OPENAI_API_KEY = "your-api-key"
   ```

2. Run the script in a Python environment.

3. Enter your messages in the console, and the AI will respond accordingly.

## Script Details

- `chat_with_openai(prompt, history)`: Sends the user input to the OpenAI API, updates the chat history, and returns the AI response.

- `save_chat_history(history, filename="chat_history.json")`: Saves the chat history to a JSON file.

- `main()`: Main function to run the chat interaction loop.

## How to Run

```bash
python PythonChat_002.py
```

## Notes

- Type 'exit' to end the conversation.

- The chat history is saved to `chat_history.json` for future reference or training.

## Dependencies

- Ensure you have the required dependencies installed. You can use the following command:

  ```bash
  pip install -r requirements.txt
  ```

## License

This script is licensed under the [MIT License](LICENSE).