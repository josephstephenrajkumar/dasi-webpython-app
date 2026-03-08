import os

from flask import Flask, request, render_template
import joblib
import os
from groq import Groq

model = joblib.load("food_expenditure_model.pkl")  
#os.environ["GROQ_API_KEY"] = ""
client = Groq()

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
@app.route("/foodExp",methods=["Get","Post"])
def foodExp():
    return(render_template("foodExp.html"))

@app.route("/FEprediction",methods=["Get","Post"])
def FEprediction():
    q=float(request.form.get("q"))
    r = model.predict([[1000]])
    return(render_template("FEprediction.html", r=r[0][0]))

@app.route("/Chatbot",methods=["Get","Post"])
def Chatbot():
    return(render_template("chatbot.html"))

@app.route("/reply",methods=["Get","Post"])
def reply():
    q=request.form.get("q")
    r = client.chat.completions.create(
        model="qwen/qwen3-32b",
        messages=[
            {"role": "system", "content": "You are a concise and professional AI Assistant."},
            {"role": "user", "content": q}
        ]
    )
    
    return(render_template("reply.html", r=r))

if __name__ == "__main__":
    app.run()
