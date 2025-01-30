from app.models.livro_model import Livro
from app.dao.livro_dao import LivroDAO
from typing import List

class LivroService:
    def __init__(self, dao: LivroDAO):
        self.dao = dao

    def listar_livros(self):
        return self.dao.listar_livros()

    def buscar_livro_por_id(self, livro_id: int):
        return self.dao.buscar_por_id(livro_id)

    def adicionar_livro(self, livro: Livro):
        return self.dao.adicionar_livro(livro)

    def atualizar_livro(self, livro_id: int, livro: Livro):
        return self.dao.atualizar_livro(livro_id, livro)

    def deletar_livro(self, livro_id: int):
        return self.dao.deletar_livro(livro_id)
