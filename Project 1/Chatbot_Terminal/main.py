
def welcome():
    """Print a welcome message when the chatbot starts."""
    print("=" * 50)
    print("       Welcome to the Rule-Based Chatbot!")
    print("  Type 'bye', 'exit', or 'quit' to stop.")
    print("=" * 50)
    print()


def normalize_input(user_input):
    """
    Normalize the user's input by converting it to lowercase
    and stripping leading/trailing whitespace.
    """
    return user_input.lower().strip()


def get_response(user_input):
    """
    Match the normalized user input against predefined rules
    and return an appropriate response string.
    """

    # --- Greetings ---
    if user_input in ("hi", "hello", "hey"):
        return "Hello! How can I help you today?"

    elif user_input == "good morning":
        return "Good morning! Hope you're having a great day."

    elif user_input == "good evening":
        return "Good evening! How can I assist you?"

    # --- Identity questions ---
    elif user_input in ("what is your name", "what's your name", "who are you"):
        return "I am your rule-based chatbot. I'm here to help!"

    elif user_input in ("how are you", "how are you doing", "how do you do"):
        return "I'm just a bot, but I'm doing great! Thanks for asking."

    elif user_input in ("what can you do", "what do you do", "help"):
        return (
            "I can answer simple questions and have a basic conversation. "
            "Try asking me about the time, my name, or just say hello!"
        )

    # --- Small talk ---
    elif user_input in ("that's great", "great", "awesome", "cool", "nice"):
        return "Glad you think so! Is there anything else I can help with?"

    elif user_input in ("thank you", "thanks", "thank you so much"):
        return "You're welcome! Feel free to ask me anything else."

    elif user_input in ("ok", "okay", "got it", "i see"):
        return "Alright! Let me know if you need anything else."

    # --- Time and date ---
    elif user_input in ("what time is it", "what's the time", "current time"):
        import datetime
        now = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is {now}."

    elif user_input in ("what is today's date", "what's today's date", "today's date", "what is the date"):
        import datetime
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {today}."

    # --- Fun / general knowledge ---
    elif user_input in ("tell me a joke", "say a joke", "joke"):
        return (
            "Why don't scientists trust atoms? "
            "Because they make up everything!"
        )

    elif user_input in ("what is python", "tell me about python"):
        return (
            "Python is a popular, beginner-friendly programming language "
            "known for its clean syntax and wide range of applications."
        )

    elif user_input in ("what is ai", "what is artificial intelligence"):
        return (
            "Artificial Intelligence is the simulation of human intelligence "
            "by machines, enabling them to learn, reason, and solve problems."
        )

    elif user_input in ("what is a chatbot", "what are you"):
        return (
            "A chatbot is a program designed to simulate conversation with humans. "
            "I am a simple rule-based chatbot — I follow predefined rules, no AI!"
        )

    # --- Farewell (handled in the loop, but kept here as safety) ---
    elif user_input in ("bye", "exit", "quit", "stop"):
        return "EXIT"

    # --- Fallback for unrecognised input ---
    else:
        return (
            "I'm sorry, I didn't understand that. "
            "Could you try rephrasing, or type 'help' to see what I can do?"
        )


def main():
    """Main loop: keep the chatbot running until an exit command is given."""
    welcome()

    while True:
        # Read input from the user
        try:
            raw_input_text = input("You: ")
        except (EOFError, KeyboardInterrupt):
            # Handle Ctrl+D or Ctrl+C gracefully
            print("\nBot: Session interrupted. Goodbye! Have a nice day.")
            break

        # Normalize the input before processing
        normalized = normalize_input(raw_input_text)

        # Skip empty input without printing anything
        if not normalized:
            print("Bot: Please type something so I can help you!\n")
            continue

        # Check for exit commands first
        if normalized in ("bye", "exit", "quit", "stop"):
            print("Bot: Goodbye! Have a nice day. 😊")
            break

        # Get and display the chatbot's response
        response = get_response(normalized)
        print(f"Bot: {response}\n")


# Entry 
if __name__ == "__main__":
    main()