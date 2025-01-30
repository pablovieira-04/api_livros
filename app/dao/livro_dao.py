from typing import List
from app.models.livro_model import Livro

class LivroDAO:
    def __init__(self):
        self.livros = []
        self.proximo_id = 1  # Contador para IDs

    def listar_livros(self):
        return self.livros

    def buscar_por_id(self, livro_id: int):
        return next((livro for livro in self.livros if livro.id == livro_id), None)

    def adicionar_livro(self, livro: Livro):
        livro.id = self.proximo_id  # Define o ID automaticamente
        self.proximo_id += 1
        self.livros.append(livro)
        return livro

    def atualizar_livro(self, livro_id: int, livro: Livro):
        for index, l in enumerate(self.livros):
            if l.id == livro_id:
                livro.id = livro_id  # Garante que o ID permanece o mesmo
                self.livros[index] = livro
                return livro
        return None

    def deletar_livro(self, livro_id: int):
        livro = self.buscar_por_id(livro_id)
        if livro:
            self.livros.remove(livro)
            return True
        return False
