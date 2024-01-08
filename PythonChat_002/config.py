# config.py

OPENAI_API_KEY = "your-api-key"
OPENAI_MODEL_NAME = "gpt-3.5-turbo"
EXIT_COMMAND = "stop chat"
OPENAI_API_ENDPOINT = "https://api.openai.com/v1/"

if not OPENAI_API_KEY:
    raise ValueError("Please provide a valid OpenAI API key.")
