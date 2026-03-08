from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/",methods=["Get","Post"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["Get","Post"])
def main():
    return(render_template("main.html"))
@app.route("/login",methods=["Get","Post"])
def login():
    return(render_template("login.html"))
@app.route("/induction",methods=["Get","Post"])
def induction():
    return(render_template("induction.html"))
@app.route("/correct",methods=["Get","Post"])
def correct():
    return(render_template("correct.html"))
@app.route("/wrong",methods=["Get","Post"])
def wrong():
    return(render_template("wrong.html"))
if __name__ == "__main__":
    app.run()
