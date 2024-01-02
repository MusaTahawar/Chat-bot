import openai

# Set your OpenAI API key
api_key = "YOUR_API_KEY"
openai.api_key = api_key

# Define a function to interact with GPT-3
def ask_gpt3(prompt):
    response = openai.ChatCompletion.create(
        model="text-davinci-003",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

# Main function to run the chatbot
def main():
    print("Welcome to the GPT-3 Chatbot!")
    print("You can start chatting. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = ask_gpt3(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
