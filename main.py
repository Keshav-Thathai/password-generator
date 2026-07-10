from flask import Flask,render_template,request
import random

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&"
    password=""
    if request.method=="POST":
      length=int(request.form["length"])
      for i in range(length):
         password+=random.choice(chars)

    return render_template("index.html",password=password)
if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000,debug=True)
    
