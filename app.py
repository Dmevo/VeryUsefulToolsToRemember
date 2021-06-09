from flask import Flask, render_template
from ferramenta import Ferramenta

app = Flask(__name__)

ferramenta_list = [Ferramenta(1 ,"PyCharm", "https://www.jetbrains.com/pt-br/pycharm/download/#section=windows", "IDE especializada para Python", ["ide", "pycharm", "python"]), 
Ferramenta(2, "Flask", "https://flask.palletsprojects.com/en/2.0.x/", "Framework para Python", ["framework", "python", "flask"]),]

@app.route("/")
def home():
    return render_template("home.html", ferramenta_list=ferramenta_list)