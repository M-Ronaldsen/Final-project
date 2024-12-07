from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/todayschoicereview")
def todayschoicereview():
    return render_template("todayschoicereview.html")

@app.route("/gameoftheweek")
def gameoftheweek():
    return render_template("gameoftheweek.html")

@app.route("/contactus")
def contactus():
    return render_template("contactus.html")



if __name__ == "__main__":
    app.run(debug=True)
