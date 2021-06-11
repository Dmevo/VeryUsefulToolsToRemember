from flask import Flask
import os
from application.model.entity.ferramenta import Ferramenta

app = Flask(__name__, static_folder = os.path.abspath("application/view/static"), template_folder = os.path.abspath("application/view/templates"))

ferramenta_list = [Ferramenta(1 ,"PyCharm", "https://www.jetbrains.com/pt-br/pycharm/download/#section=windows", "IDE especializada para Python", ["ide", "pycharm", "python"]), 
Ferramenta(2, "Flask", "https://flask.palletsprojects.com/en/2.0.x/", "Framework para Python", ["framework", "python", "flask"]),]

from application.controller import home_controller