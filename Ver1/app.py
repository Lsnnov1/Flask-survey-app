from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.config["SECRET_KEY"] = "This is a secret"


RESPONSES = []

@app.route("/")
def show_homepage():
    """Renders root page"""
    session[RESPONSES] = []
    return render_template("index.html")

@app.route("/Questions/<qindex>")
def show_q1(qindex):
    """Displays first question form"""
    if qindex == "q1":
        return render_template("question1.html")
    else: 
        return redirect("/Questions/q1")

@app.route("/Questions/<qindex>")
def show_q2(qindex):
    """Displays second question form"""
    if qindex == "q2":
        session["q1"] = request.args["q1"]
        RESPONSES.append(session["q1"])
        return render_template("question2.html", q1=session["q1"] )
    else: 
        return redirect("/Questions/q1")

@app.route("/Questions/<qindex>")
def show_q3(qindex):
    """Displays third question form"""
    if qindex == "q3":
        session["q2"] = request.args["q2"]
        RESPONSES.append(session["q2"])
        return render_template("question3.html", q1=session["q1"], q2=session["q2"])
    else:
        return redirect("/Questions/q1")
    

@app.route("/Questions/<qindex>")
def show_q4(qindex):
    """Displays fourth question form"""
    if qindex == "q4":
        session["q3"] = request.args["q3"]
        RESPONSES.append(session["q3"])
        return render_template("question4.html", q1=session["q1"], q2=session["q2"], q3=session["q3"])
    else: 
        return redirect("/Questions/q1")


@app.route("/ThankYou")
def thank_user():
    """Returns a "thank you" route"""
    session["q4"] = request.args["q4"]
    RESPONSES.append(session["q4"])
    return render_template("thankyou.html", q1=session["q1"], q2=session["q2"],q3=session["q3"], q4=session["q4"], response_list = RESPONSES)

