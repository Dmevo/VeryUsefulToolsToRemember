from flask import Flask, render_template, request
from ferramenta import Ferramenta

app = Flask(__name__)

ferramenta_list = [Ferramenta(1 ,"PyCharm", "https://www.jetbrains.com/pt-br/pycharm/download/#section=windows", "IDE especializada para Python", ["ide", "pycharm", "python"]), 
Ferramenta(2, "Flask", "https://flask.palletsprojects.com/en/2.0.x/", "Framework para Python", ["framework", "python", "flask"]),]

#ferramenta_list = []

@app.route("/", methods=['GET'])
def home():
    return render_template("home.html", ferramenta_list=ferramenta_list)

@app.route("/adicionar", methods=['POST'])
def adicionar():
    nome = request.form.get('nome', None)
    url = request.form.get('url', None)
    descricao = request.form.get('descricao', None)
    tag = request.form.get('tag', None)
    id = len(ferramenta_list) + 1
    ferramenta = Ferramenta(id, nome, url, descricao, tag)
    ferramenta_list.append(ferramenta)
    return render_template("home.html", ferramenta_list=ferramenta_list)

@app.route("/excluir/<id>", methods=['GET'])
def excluir(id):
    for ferramenta in ferramenta_list:
        if ferramenta.get_id() == int(id):
            ferramenta_list.remove(ferramenta)
            return render_template("home.html", ferramenta_list=ferramenta_list)
    return render_template("home.html", ferramenta_list=ferramenta_list), 404

@app.route("/busca", methods=['GET'])
def busca():
    ferramenta_list_filtrado = []
    pesquisa = request.args.get('pesquisa')
    pesquisa_tag = request.args.get('tag', None)
    for ferramenta in ferramenta_list:
        if pesquisa_tag == "pesquisar-tag":
            if pesquisa in ferramenta.get_tag():
                ferramenta_list_filtrado.append(ferramenta)
        elif pesquisa_tag == None:
            if pesquisa in ferramenta.get_nome() or pesquisa in ferramenta.get_descricao():
                ferramenta_list_filtrado.append(ferramenta)


    return render_template("home.html", ferramenta_list=ferramenta_list_filtrado)

            