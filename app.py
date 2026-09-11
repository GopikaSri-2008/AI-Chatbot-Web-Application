from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def get_response(message):
    msg = message.lower().strip()
    replies = []

    # GREETING
    if any(word in msg for word in ["hi", "hello", "hey", "hai"]):
        replies.append(
            "👋 <strong>Hello! I'm StudyNest AI.</strong><br>"
            "I'm here to help you understand programming and computer science "
            "topics in a simple way."
        )

    # PYTHON
    if "python" in msg:
        replies.append(
            "🐍 <strong>Python</strong><br><br>"
            "<strong>Definition:</strong> Python is a high-level, interpreted "
            "programming language known for its simple and readable syntax."
            "<br><br>"
            "<strong>Key Features:</strong><br>"
            "• Easy to learn and use<br>"
            "• Object-oriented programming support<br>"
            "• Large standard library<br>"
            "• Used in web development, AI, data science and automation"
            "<br><br>"
            "<strong>Example:</strong><br>"
            "<pre>print(\"Hello World\")</pre>"
            "<strong>Output:</strong> Hello World"
        )

    # JAVA
    if "java" in msg:
        replies.append(
            "☕ <strong>Java</strong><br><br>"
            "<strong>Definition:</strong> Java is a high-level, object-oriented "
            "programming language used to develop desktop, web and mobile applications."
            "<br><br>"
            "<strong>Key Features:</strong><br>"
            "• Object-oriented<br>"
            "• Platform independent<br>"
            "• Secure and robust<br>"
            "• Supports multithreading"
            "<br><br>"
            "<strong>Example:</strong><br>"
            "<pre>class Demo {\n"
            "    public static void main(String[] args) {\n"
            "        System.out.println(\"Hello World\");\n"
            "    }\n"
            "}</pre>"
        )

    # HTML
    if "html" in msg:
        replies.append(
            "🌐 <strong>HTML</strong><br><br>"
            "<strong>Definition:</strong> HTML stands for HyperText Markup Language. "
            "It is used to create the structure and content of web pages."
            "<br><br>"
            "<strong>Common Elements:</strong><br>"
            "• Headings<br>"
            "• Paragraphs<br>"
            "• Links<br>"
            "• Images<br>"
            "• Forms"
            "<br><br>"
            "<strong>Example:</strong><br>"
            "<pre>&lt;h1&gt;Hello World&lt;/h1&gt;</pre>"
        )

    # CSS
    if "css" in msg:
        replies.append(
            "🎨 <strong>CSS</strong><br><br>"
            "<strong>Definition:</strong> CSS stands for Cascading Style Sheets. "
            "It is used to style and design HTML web pages."
            "<br><br>"
            "<strong>CSS can control:</strong><br>"
            "• Colors<br>"
            "• Fonts<br>"
            "• Spacing<br>"
            "• Layout<br>"
            "• Responsive design"
            "<br><br>"
            "<strong>Example:</strong><br>"
            "<pre>h1 {\n"
            "    color: purple;\n"
            "    font-size: 30px;\n"
            "}</pre>"
        )

    # JAVASCRIPT
    if "javascript" in msg:
        replies.append(
            "⚡ <strong>JavaScript</strong><br><br>"
            "<strong>Definition:</strong> JavaScript is a programming language "
            "mainly used to make web pages interactive and dynamic."
            "<br><br>"
            "<strong>Uses:</strong><br>"
            "• Button interactions<br>"
            "• Form validation<br>"
            "• Dynamic content<br>"
            "• Animations<br>"
            "• Web applications"
            "<br><br>"
            "<strong>Example:</strong><br>"
            "<pre>console.log(\"Hello World\");</pre>"
        )

    # FLASK
    if "flask" in msg:
        replies.append(
            "🚀 <strong>Flask</strong><br><br>"
            "<strong>Definition:</strong> Flask is a lightweight Python web "
            "framework used to build web applications and APIs."
            "<br><br>"
            "<strong>Advantages:</strong><br>"
            "• Simple and flexible<br>"
            "• Easy to learn<br>"
            "• Supports routing<br>"
            "• Useful for small and medium web applications"
            "<br><br>"
            "<strong>Basic Example:</strong><br>"
            "<pre>from flask import Flask\n\n"
            "app = Flask(__name__)\n\n"
            "@app.route(\"/\")\n"
            "def home():\n"
            "    return \"Hello World\"</pre>"
        )

    # PROGRAMMING
    if "programming" in msg or "coding" in msg:
        replies.append(
            "💻 <strong>Programming</strong><br><br>"
            "Programming is the process of writing instructions that tell "
            "a computer how to perform a specific task."
            "<br><br>"
            "<strong>Basic programming process:</strong><br>"
            "1. Understand the problem<br>"
            "2. Plan the solution<br>"
            "3. Write the code<br>"
            "4. Test the program<br>"
            "5. Fix errors and improve the code"
        )

    # OOP
    if "oop" in msg or "object oriented" in msg:
        replies.append(
            "📚 <strong>Object-Oriented Programming (OOP)</strong><br><br>"
            "OOP is a programming approach based on objects and classes."
            "<br><br>"
            "<strong>Main Concepts:</strong><br>"
            "• <strong>Encapsulation:</strong> Combining data and methods into a single unit.<br>"
            "• <strong>Inheritance:</strong> Acquiring properties and methods from another class.<br>"
            "• <strong>Polymorphism:</strong> One interface with different implementations.<br>"
            "• <strong>Abstraction:</strong> Hiding unnecessary implementation details."
        )

    # DBMS
    if "dbms" in msg or "database" in msg:
        replies.append(
            "🗄️ <strong>DBMS</strong><br><br>"
            "<strong>Definition:</strong> DBMS stands for Database Management System. "
            "It is software used to store, manage, organize and retrieve data."
            "<br><br>"
            "<strong>Examples:</strong><br>"
            "• MySQL<br>"
            "• Oracle<br>"
            "• PostgreSQL<br>"
            "• Microsoft Access"
            "<br><br>"
            "<strong>Advantages:</strong><br>"
            "• Reduces data redundancy<br>"
            "• Provides data security<br>"
            "• Makes data management easier"
        )

    # THANKS
    if "thank" in msg:
        replies.append(
            "😊 <strong>You're welcome!</strong><br>"
            "Keep learning and keep practicing. You've got this! 💜"
        )

    # GOODBYE
    if "bye" in msg:
        replies.append(
            "👋 <strong>Goodbye!</strong><br>"
            "Keep learning, keep practicing and keep coding! 🌱"
        )

    # DEFAULT
    if not replies:
        replies.append(
            "🤖 <strong>I'm still learning!</strong><br><br>"
            "Try asking me about:<br>"
            "🐍 Python • ☕ Java • 🌐 HTML • 🎨 CSS<br>"
            "⚡ JavaScript • 🚀 Flask • 📚 OOP • 🗄️ DBMS"
        )

    return "<br><br>".join(replies)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}

    message = data.get("message", "").strip()

    if not message:
        return jsonify({
            "response": "Please enter a question so I can help you. 😊"
        })

    return jsonify({
        "response": get_response(message)
    })


if __name__ == "__main__":
    app.run(debug=True)
