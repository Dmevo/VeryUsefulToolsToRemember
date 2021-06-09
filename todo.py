
class ToDo:
    
    def __init__(self, nome=None, link=None, descricao=None, tag=None):
        self.nome = nome
        self.link = link
        self.descricao = descricao
        self.tag = []

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_link(self, link):
        self.link = link

    def get_link(self):
        return self.link

    def set_descricao(self, descricao):
        self.descricao = descricao
    
    def get_descricao(self):
        return self.descricao

    def set_tag(self, tag):
        self.tag.append(tag)
    
    def get_tag(self):
        return self.tag