import openai

# key empty due security regulations from github
openai.api_key = " "

def generate_text(text):
    resp = openai.Completion.create(
        engine = "gpt-4o-mini",
        prompt = text,
        max_tokens = 150,
        n = 5,
        stop = None,
        temperature = 0.8,
    )
    return resp.choices[0].text.strip()

def main():
    print("\n Welcome to Chatbot!")
    print("Type exit any moment to leave the chat")

    while True:
        user_message = input("\nAsk me something: ")
        if user_message.lower() == "exit":
            break    
        gpt4_prompt = f"\nAsk: {user_message}"
        chatbot_response = generate_text(gpt4_prompt)
        print(f"\nChatbot: {chatbot_response}")

if __name__ == "__main__":
    main()