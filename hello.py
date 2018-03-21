from flask import Flask, render_template

app = Flask("MyApp")

@app.route("/")
def hello():
    return "Hello Mirela!"

@app.route("/idontexist")
def idontexist():
    return "I do exist now!"

@app.route("/georgie")
def georgie():
    return "I'm hungry"

app.run(debug=True)