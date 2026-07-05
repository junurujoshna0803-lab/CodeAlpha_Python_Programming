print("=" * 45)
print("🤖 BASIC CHATBOT")
print("=" * 45)
print("Type 'bye' anytime to exit.\n")

while True:

    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! Nice to meet you.")

    elif user == "hi":
        print("Bot: Hi! How are you today?")

    elif user == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    elif user == "what is your name":
        print("Bot: My name is CodeAlpha ChatBot.")

    elif user == "who created you":
        print("Bot: I was created using Python.")

    elif user == "bye":
        print("Bot: Goodbye! Have a wonderful day.")
        break

    else:
        print("Bot: Sorry, I don't understand that. Please try another question.")