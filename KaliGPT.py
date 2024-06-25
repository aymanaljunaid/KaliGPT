# KaliGPT.py
import os
import openai

def ask_openai(question):
    # Ensure the API key is fetched properly from environment variables
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set.")
    
    openai.api_key = api_key

    # Adjusted API call according to the latest syntax changes
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    
    # Corrected response extraction according to the latest library structure
    return response['choices'][0]['message']['content']

def chat():
    print("Type 'exit' to stop the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = ask_openai(user_input)
        print(f"KaliGPT: {response}")

if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("OPENAI_API_KEY is not set in your environment variables.")
        print("Set the API key as an environment variable for security.")
        os._exit(1)
    chat()
