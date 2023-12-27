import json
from os import path
from config import OPENAI_API_KEY
from openai import OpenAI

api_key = OPENAI_API_KEY
client = OpenAI(api_key=api_key)

def chat_with_openai(prompt, history):
    """
    Sends the prompt to OpenAI API and returns the AI response.
    Also updates the chat history with the new message pair.
    """
    # Add the user input to the chat history
    history.append({"role": "user", "content": prompt})

    # Make the API call with the chat history
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            *history
        ]
    )

    # Get the AI response from the API
    ai_response = response.choices[0].message.content

    # Add the AI response to the chat history
    history.append({"role": "assistant", "content": ai_response})

    return ai_response

def save_chat_history(history, filename="chat_history.json"):
    """
    Saves the chat history to a JSON file.
    """
    with open(filename, "w") as file:
        json.dump(history, file)

def main():
    # Initialize an empty list to store the chat history
    chat_history = []

    print("Welcome to the ChatBot! Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Call the OpenAI API
        ai_response = chat_with_openai(user_input, chat_history)

        # Print the AI response
        print(f"AI: {ai_response}")

    # Save the chat history to a file for future reference or training
    save_chat_history(chat_history)

if __name__ == "__main__":
    main()
