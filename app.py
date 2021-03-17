from flask import Flask, redirect, request, render_template, url_for, session

app = Flask(__name__, static_folder = "static", static_url_path = "/")
app.secret_key = "aijadrkyac"

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/member/')
def mem():
    if "act" in session:
        return render_template("member.html")
    else:
        return redirect('/')

@app.route('/error/')
def err():
    return render_template("error.html")

@app.route('/signin', methods=["POST"])
def link():
    act = request.form["act"]
    pas = request.form["pas"]
    session["act"] = "test"
    session["pas"] = "test"
    if act == "test" and pas == "test":
        return redirect("/member/")
    else:
        return redirect("/error/")

@app.route('/signout')
def out():
    session.pop('act', None)
    session.pop('pas', None)
    return redirect('/')


app.run(port = 3000)