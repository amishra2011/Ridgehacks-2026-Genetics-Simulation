from flask import Flask, render_template, redirect, url_for, request, jsonify, session
import requests
import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))


@app.route("/")
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template("Home Page/homepage.html")


@app.route("/region")
def region():
    if 'user' not in session:
        return redirect(url_for('login'))
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


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        try:
            res = supabase.auth.sign_in_with_password(
                {"email": email, "password": password})
            session['user'] = res.user.email
            return redirect(url_for('home'))
        except Exception as e:
            return render_template("Auth Page/login.html", error="Invalid email or password")
    return render_template("Auth Page/login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        try:
            res = supabase.auth.sign_up({"email": email, "password": password})
            session['user'] = res.user.email
            return redirect(url_for('home'))
        except Exception as e:
            print("SIGNUP ERROR:", e)
            return render_template("Auth Page/signup.html", error=str(e))
    return render_template("Auth Page/signup.html")


@app.route("/google-login")
def google_login():
    res = supabase.auth.sign_in_with_oauth({"provider": "google"})
    return redirect(res.url)


@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


@app.route('/api/explain-mutation', methods=['POST'])
def explain_mutation():
    data = request.json
    GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"
    response = requests.post(
        f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}",
        headers={"Content-Type": "application/json"},
        json={"contents": [{"parts": [{"text": data['prompt']}]}]}
    )
    result = response.json()
    text = result['candidates'][0]['content']['parts'][0]['text']
    return jsonify({"text": text})


if __name__ == "__main__":
    app.run(debug=False, port=5000)
