const chatBox = document.getElementById("chatBox");
const input = document.getElementById("messageInput");
const form = document.getElementById("chatForm");
const welcome = document.getElementById("welcome");


function getTime() {
    return new Date().toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit"
    });
}


function addMessage(text, sender) {

    const message = document.createElement("div");

    message.className = "message " + sender;


    const avatar = document.createElement("div");

    avatar.className = "avatar";

    avatar.textContent =
        sender === "bot" ? "✦" : "You";


    const content = document.createElement("div");

    content.className = "message-content";


    const head = document.createElement("div");

    head.className = "message-head";

    head.innerHTML =
        `<strong>${sender === "bot" ? "StudyNest AI" : "You"}</strong>
         <span class="time">${getTime()}</span>`;


    const bubble = document.createElement("div");

    bubble.className = "bubble";


    if (sender === "bot") {
        bubble.innerHTML = text;
    } else {
        bubble.textContent = text;
    }


    content.appendChild(head);
    content.appendChild(bubble);

    message.appendChild(avatar);
    message.appendChild(content);

    chatBox.appendChild(message);

    chatBox.scrollTop = chatBox.scrollHeight;
}


function showTyping() {

    const typing = document.createElement("div");

    typing.id = "typing";

    typing.className = "message bot";

    typing.innerHTML = `
        <div class="avatar">✦</div>

        <div class="message-content">
            <div class="typing">
                StudyNest AI is typing...
            </div>
        </div>
    `;

    chatBox.appendChild(typing);

    chatBox.scrollTop = chatBox.scrollHeight;
}


function removeTyping() {

    const typing =
        document.getElementById("typing");

    if (typing) {
        typing.remove();
    }
}


form.addEventListener("submit", async (e) => {

    e.preventDefault();

    const message = input.value.trim();

    if (!message) {
        return;
    }


    welcome.style.display = "none";

    addMessage(message, "user");

    input.value = "";

    showTyping();


    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });


        const data = await response.json();

        removeTyping();

        addMessage(data.response, "bot");

    }

    catch (error) {

        removeTyping();

        addMessage(
            "Sorry, something went wrong. Please try again.",
            "bot"
        );

    }

});


function quickMessage(message) {

    input.value = message;

    form.dispatchEvent(
        new Event("submit", {
            bubbles: true,
            cancelable: true
        })
    );
}


function clearChat() {

    chatBox.innerHTML = "";

    chatBox.appendChild(welcome);

    welcome.style.display = "block";

    addMessage(
        "Hello! 👋 I'm StudyNest AI. Ask me anything about your study topics.",
        "bot"
    );
}


function toggleTheme() {

    document.body.classList.toggle("dark");

    localStorage.setItem(
        "studynestTheme",
        document.body.classList.contains("dark")
            ? "dark"
            : "light"
    );
}


function toggleSidebar() {

    document
        .getElementById("sidebar")
        .classList.toggle("open");
}


if (localStorage.getItem("studynestTheme") === "dark") {

    document.body.classList.add("dark");

}