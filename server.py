from flask import Flask, render_template, redirect, request, session, flash
import random
app = Flask(__name__)
app.secret_key = "SECRET_KEY"

@app.route("/")
def index(): 
    if not session.has_key("randomNumber"):

        session["randomNumber"] = random.randrange(1,4)

    return render_template ("index.html", randomNumber = session["randomNumber"])

@app.route("/number", methods=["POST"])
def guess_the_number():

    if(len(request.form["number"]) < 1):
        print "Please enter a number"
        flash("Please enter a number")

    else:
        session["number"] = int(request.form["number"])

        if (session["number"] == session["randomNumber"]):
            print "You got it!!"
        elif(session["number"] > session["randomNumber"]):
            print "The Number is Too High"
            flash("The Number is Too High")
        elif(session["number"] < session["randomNumber"]):
            print "The Number is Too Low"
            flash("The Number is Too Low")

        
            


    return redirect ("/")

@app.route("/reset")
def reset_session():
    session.clear()

    return redirect("/")



app.run(debug=True)