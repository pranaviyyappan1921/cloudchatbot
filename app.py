from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "").lower()

    if "hello" in message or "hi" in message:
        response = "Hello! How can I help you?"

    elif "cloud computing" in message:
        response = "Cloud computing is the delivery of computing services such as servers, storage and software over the internet."

    elif "azure" in message:
        response = "Microsoft Azure is a cloud computing platform that provides services such as computing, storage, databases and networking."

    elif "who are you" in message:
        response = "I am a simple cloud-based chatbot."

    else:
        response = "Sorry, I don't understand that question yet."

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)