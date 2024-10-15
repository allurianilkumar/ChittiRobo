from transformers import pipeline

# Load the GPT-2 model
chatbot = pipeline("text-generation", model="gpt2")

def chat_with_gpt():
    print("Welcome to your chatbot! Type 'exit' to quit.")
    
    # Keep track of conversation history
    conversation_history = ""

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        
        # Append user input to conversation history
        conversation_history += f"You: {user_input}\n"

        # Generate a response with truncation and padding settings
        response = chatbot(
            conversation_history,
            max_new_tokens=50,        # Specify the number of new tokens to generate
            num_return_sequences=1,
            truncation=True,           # Explicitly enable truncation
            pad_token_id=50256        # Set pad_token_id for GPT-2
        )
        
        bot_reply = response[0]['generated_text'].strip()

        # Print the bot's reply
        print("Chatbot:", bot_reply)

        # Append bot reply to conversation history
        conversation_history += f"Chatbot: {bot_reply}\n"

if __name__ == "__main__":
    chat_with_gpt()
