from flask import render_template, url_for, request
from application import app
from application.model.entity.ferramenta import Ferramenta
from application.model.dao.ferramentaDAO import FerramentaDAO

@app.route("/", methods=['GET'])
def home():
    ferramenta_dao = FerramentaDAO()
    ferramenta_list = ferramenta_dao.mostrar_ferramentas()
    return render_template("home.html", ferramenta_list=ferramenta_list)

@app.route("/adicionar", methods=['POST'])
def adicionar():
    ferramenta_dao = FerramentaDAO()
    ferramenta_list = ferramenta_dao.mostrar_ferramentas()
    nome = request.form.get('nome', None)
    url = request.form.get('url', None)
    descricao = request.form.get('descricao', None)
    tag = request.form.get('tag', None)
    id = len(ferramenta_list) + 1
    tag_list = tag.split(", ")
    ferramenta = Ferramenta(id, nome, url, descricao, tag_list)
    ferramenta_list.append(ferramenta)
    return render_template("home.html", ferramenta_list=ferramenta_list)

@app.route("/excluir/<id>", methods=['GET'])
def excluir(id):
    ferramenta_dao = FerramentaDAO()
    ferramenta_list = ferramenta_dao.mostrar_ferramentas()
    for ferramenta in ferramenta_list:
        if ferramenta.get_id() == int(id):
            ferramenta_list.remove(ferramenta)
            return render_template("home.html", ferramenta_list=ferramenta_list)
    return render_template("home.html", ferramenta_list=ferramenta_list), 404

@app.route("/busca", methods=['GET'])
def busca():
    ferramenta_dao = FerramentaDAO()
    ferramenta_list = ferramenta_dao.mostrar_ferramentas()
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