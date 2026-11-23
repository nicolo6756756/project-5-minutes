
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>PROJECT 5 MINUTES</title>

<style>
* { box-sizing: border-box; }

body {
    margin: 0;
    background: #101014;
    color: white;
    font-family: Arial, sans-serif;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
}

#content { padding: 25px; }

h1 { font-size: 28px; }

#timer {
    font-size: clamp(65px, 15vw, 100px);
    color: #00ff99;
    font-weight: bold;
    margin: 35px 0;
}

#message { color: #aaa; }

#finale {
    display: none;
    position: fixed;
    inset: 0;
    background: #101014;
    align-items: center;
    justify-content: center;
    padding: 20px;
    font-size: clamp(35px, 9vw, 75px);
    font-weight: 900;
    color: #ff4d9d;
}
</style>
</head>

<body>
<div id="content">
    <h1>PROJECT 5 MINUTES</h1>
    <p id="message">Qualcosa sta per succedere...</p>
    <div id="timer">05:00</div>
</div>

<div id="finale">SO CHE SEI GAY 🌈</div>

<script>
let remaining = 300;

const timer = document.getElementById("timer");
const finale = document.getElementById("finale");

const countdown = setInterval(() => {
    remaining--;

    const minutes = Math.floor(remaining / 60);
    const seconds = remaining % 60;

    timer.textContent =
        String(minutes).padStart(2, "0") + ":" +
        String(seconds).padStart(2, "0");

    if (remaining <= 0) {
        clearInterval(countdown);
        document.getElementById("content").style.display = "none";
        finale.style.display = "flex";
    }
}, 1000);
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
