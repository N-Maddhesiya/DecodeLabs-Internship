# Chatbot Project Main File
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def normalize_input(text):
    return text.strip().lower()

def get_bot_response(message):
    if message in ["hi", "hello", "hey", "good morning", "good evening"]:
        return "Hello! How can I help you?"
    elif message in ["bye", "exit", "quit", "stop"]:
        return "Goodbye! Have a nice day."
    elif message in ["how are you", "how are you?", "what's up", "whats up"]:
        return "I am fine, thank you. How can I assist you?"
    elif message in ["what is your name", "who are you"]:
        return "I am a simple rule-based AI chatbot."
    elif message in ["help", "what can you do"]:
        return "I can respond to greetings, simple questions, and exit commands."
    elif message in ["thank you", "thanks", "thx"]:
        return "You're welcome!"
    else:
        return "I did not understand that. Please try again."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    normalized = normalize_input(user_message)
    response = get_bot_response(normalized)
    exit_chat = normalized in ["bye", "exit", "quit", "stop"]
    return jsonify({"response": response, "exit": exit_chat})

if __name__ == "__main__":
    app.run(debug=True)