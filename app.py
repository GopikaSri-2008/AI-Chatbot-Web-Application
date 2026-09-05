from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def get_response(message):
    msg = message.lower().strip()
    replies = []

    if any(word in msg for word in ["hi", "hello", "hey", "hai"]):
        replies.append("Hello! 👋 I'm StudyNest AI. How can I help you today?")

    if "python" in msg:
        replies.append("🐍 Python is a simple and powerful programming language used in web development, AI, data science and automation.")

    if "java" in msg:
        replies.append("☕ Java is an object-oriented programming language widely used for application and web development.")

    if "html" in msg:
        replies.append("🌐 HTML stands for HyperText Markup Language. It is used to create the structure of web pages.")

    if "css" in msg:
        replies.append("🎨 CSS stands for Cascading Style Sheets. It is used to style and design web pages.")

    if "javascript" in msg:
        replies.append("⚡ JavaScript is used to make web pages interactive and dynamic.")

    if "flask" in msg:
        replies.append("🚀 Flask is a lightweight Python web framework used to build web applications and APIs.")

    if "programming" in msg or "coding" in msg:
        replies.append("💻 Programming means writing instructions for a computer to perform a task.")

    if "oop" in msg or "object oriented" in msg:
        replies.append("📚 OOP stands for Object-Oriented Programming. Its main concepts are Encapsulation, Inheritance, Polymorphism and Abstraction.")

    if "dbms" in msg or "database" in msg:
        replies.append("🗄️ DBMS stands for Database Management System. It is used to store, manage and retrieve data.")

    if "thank" in msg:
        replies.append("You're welcome! 😊")

    if "bye" in msg:
        replies.append("Goodbye! 👋 Keep learning and keep coding!")

    if not replies:
        replies.append("🤖 I'm still learning! Try asking me about Python, Java, HTML, CSS, JavaScript, Flask, OOP or DBMS.")

    return "<br><br>".join(replies)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    message = data.get("message", "")
    return jsonify({"response": get_response(message)})
if __name__ == "__main__":
    app.run(debug=True)