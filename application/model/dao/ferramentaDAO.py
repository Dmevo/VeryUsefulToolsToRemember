from application import ferramenta_list
from application.model.entity.ferramenta import Ferramenta

class FerramentaDAO:

    def __init__(self):
        self.ferramenta_list = ferramenta_list

    def mostrar_ferramentas(self):
        return self.ferramenta_list