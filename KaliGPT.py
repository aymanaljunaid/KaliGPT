import os
import openai
from config import OPENAI_API_KEY  # Import API key from the configuration file
import textwrap

def ask_openai(question):
    # Set the API key from the configuration file
    openai.api_key = OPENAI_API_KEY

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are KaliGPT, an AI Tool developed by Ayman Al-Junaid. You are powerful, insightful, and provide detailed, helpful responses."},
            {"role": "user", "content": question}
        ]
    )
    
    return response['choices'][0]['message']['content']

def print_stylish(label, message, color_code):
    wrapped_message = textwrap.fill(message, width=80)
    print(f"\033[{color_code}m{label}\033[0m {wrapped_message}")

def chat():
    print("\n\033[1;36mWelcome to KaliGPT! Type 'exit' to stop the chat.\033[0m\n")
    while True:
        user_input = input("\033[1;32mYou:\033[0m ")  # Green text for user input
        if user_input.lower() == 'exit':
            print("\n\033[1;31mGoodbye!\033[0m\n")  # Red text for goodbye message
            break
        response = ask_openai(user_input)
        print_stylish("KaliGPT:", response, "1;34")  # Blue text for KaliGPT response with stylish formatting

if __name__ == "__main__":
    chat()
