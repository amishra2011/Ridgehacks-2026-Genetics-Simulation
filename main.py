from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("Region Page/region.html")


@app.route("/landing")
def profile():
    return render_template("Landing Page/landingPage.html")


if __name__ == "__main__":
    app.run(debug=False, port=5000)
