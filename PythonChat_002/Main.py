import json
import logging
import requests
from os import path
from config import EXIT_COMMAND, OPENAI_API_KEY, OPENAI_MODEL_NAME, OPENAI_API_ENDPOINT
from openai import OpenAI , OpenAIError

api_key = OPENAI_API_KEY
client = OpenAI(api_key=api_key)

def chat_with_openai(prompt, history):
    history.append({"role": "user", "content": prompt})

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }

    data = {
        "model": OPENAI_MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            *history
        ]
    }

    try:
        response = requests.post(OPENAI_API_ENDPOINT + "chat/completions", json=data, headers=headers, verify=True)
        response.raise_for_status()
        response_json = response.json()
        ai_response = response_json["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        logging.error(f"Error during API call: {e}")
        return "I'm sorry, but I encountered an error during the conversation."
    except OpenAIError as e:
        logging.error(f"OpenAI API error: {e}")
        return "I'm sorry, but I encountered an error during the conversation."

    # Example: Check for specific conditions in the AI response
    if "Can you provide more details about" in ai_response:
        # Example: Ask a follow-up question
        follow_up_question = input(f"AI: {ai_response} ")
        history.append({"role": "user", "content": follow_up_question})
        return f"User: {follow_up_question}"

    history.append({"role": "assistant", "content": ai_response})
    return ai_response

def save_chat_history(history, filename="chat_history.json"):
    with open(filename, "w") as file:
        json.dump(history, file)

def show_help():
    help_message = (
        "\033[1;32mYou can interact with the ChatBot by typing messages.\033[0m\n"
        "\033[1;34mType 'exit' to end the conversation.\033[0m\n"
        "\033[1;36mAdditionally, you can type 'help' for assistance.\033[0m"
    )
    print(f"AI: \n{help_message}")

def show_chat_history(history, max_display=5):
    print("AI: Here is the recent chat history:")

    start_index = max(0, len(history) - max_display)
    end_index = len(history)
    
    for message in history[start_index:end_index]:
        role = message["role"]
        content = message["content"]
        print(f"{role.capitalize()}: {content}")

    print(f"AI: Displaying the most recent {min(len(history), max_display)} entries.")

def load_chat_history(filename="chat_history.json"):
    try:
        with open(filename, "r") as file:
            history = json.load(file)
        return history
    except FileNotFoundError:
        return []
    except Exception as e:
        logging.error(f"Error loading chat history: {e}")
        return []

def main():
    chat_history = load_chat_history()
    print("Welcome to the ChatBot! Type 'exit' to end the conversation.")

    def is_valid_input(user_input):
        return user_input.strip() != '' or user_input.lower() == 'history'

    while True:
        user_input = input("User: ")

        if not is_valid_input(user_input):
            print("Please provide a valid input. Type 'help' for assistance.")
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
    