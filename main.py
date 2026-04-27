from flask import Flask, render_template, redirect, url_for, request, jsonify
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("Home Page/homepage.html")


@app.route("/region")
def region():
    return render_template("Region Page/region.html")


@app.route("/information")
def information():
    return render_template("Information Page/info.html")


@app.route("/landing")
def profile():
    return render_template("Landing Page/landingPage.html")


@app.route("/interactive")
def interactive():
    return render_template("Interactive Page/simulation.html")


@app.route('/api/explain-mutation', methods=['POST'])
def explain_mutation():
    data = request.json
    GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"

    response = requests.post(
        f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}",
        headers={"Content-Type": "application/json"},
        json={
            "contents": [
                {
                    "parts": [{"text": data['prompt']}]
                }
            ]
        }
    )

    result = response.json()
    text = result['candidates'][0]['content']['parts'][0]['text']
    return jsonify({"text": text})


if __name__ == "__main__":
    app.run(debug=False, port=5000)
