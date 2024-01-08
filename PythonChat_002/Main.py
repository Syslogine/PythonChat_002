import json
import logging
from os import path
from config import EXIT_COMMAND, OPENAI_API_KEY, OPENAI_MODEL_NAME
from openai import OpenAI

api_key = OPENAI_API_KEY
client = OpenAI(api_key=api_key)

def chat_with_openai(prompt, history):
    history.append({"role": "user", "content": prompt})
    try:
        response = client.chat.completions.create(
            model=OPENAI_MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                *history
            ]
        )
    except Exception as e:
        logging.error(f"Error during API call: {e}")
        return "I'm sorry, but I encountered an error."

    if response.choices and response.choices[0].message and response.choices[0].message.content:
        ai_response = response.choices[0].message.content
    else:
        logging.warning("Invalid AI response content.")
        ai_response = "I'm sorry, but I couldn't generate a valid response."

    history.append({"role": "assistant", "content": ai_response})

    return ai_response

def save_chat_history(history, filename="chat_history.json"):
    with open(filename, "w") as file:
        json.dump(history, file)

def load_chat_history(filename="chat_history.json"):
    if path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return []

def show_help():
    help_message = (
        "\033[1;32mYou can interact with the ChatBot by typing messages.\033[0m\n"
        "\033[1;34mType 'exit' to end the conversation.\033[0m\n"
        "\033[1;36mAdditionally, you can type 'help' for assistance.\033[0m"
    )
    print(f"AI: \n{help_message}")

def show_chat_history(history):
    print("AI: Here is the recent chat history:")
    for message in history:
        role = message["role"]
        content = message["content"]
        print(f"{role.capitalize()}: {content}")

def main():
    chat_history = load_chat_history()
    print("Welcome to the ChatBot! Type 'exit' to end the conversation.")

    def is_valid_input(user_input):
        return user_input.strip() != "" or user_input.lower() == 'history'

    while True:
        user_input = input("User: ")

        if not is_valid_input(user_input):
            print("Please provide a valid input.")
            continue

        if user_input.lower() == EXIT_COMMAND:
            print("Goodbye!")
            break
        elif user_input.lower() == 'help':
            show_help()
        elif user_input.lower() == 'history':
            show_chat_history(chat_history)
        else:
            ai_response = chat_with_openai(user_input, chat_history)
            print(f"AI: {ai_response}")

    save_chat_history(chat_history)

if __name__ == "__main__":
    main()
