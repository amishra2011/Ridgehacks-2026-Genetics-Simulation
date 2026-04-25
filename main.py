from flask import Flask, render_template, redirect, url_for


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


if __name__ == "__main__":
    app.run(debug=False, port=5000)
