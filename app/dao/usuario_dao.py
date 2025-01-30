from typing import List
from app.models.usuario_model import Usuario

class UsuarioDAO:
    def __init__(self):
        self.usuarios = []
        self.proximo_id = 1  # Contador para IDs

    def listar_usuarios(self):
        return self.usuarios

    def buscar_por_id(self, usuario_id: int):
        return next((usuario for usuario in self.usuarios if usuario.id == usuario_id), None)

    def adicionar_usuario(self, usuario: Usuario):
        usuario.id = self.proximo_id  # Define o ID automaticamente
        self.proximo_id += 1
        self.usuarios.append(usuario)
        return usuario

    def atualizar_usuario(self, usuario_id: int, usuario: Usuario):
        for index, l in enumerate(self.usuarios):
            if l.id == usuario_id:
                usuario.id = usuario_id  # Garante que o ID permanece o mesmo
                self.usuarios[index] = usuario
                return usuario
        return None

    def deletar_usuario(self, usuario_id: int):
        usuario = self.buscar_por_id(usuario_id)
        if usuario:
            self.usuarios.remove(usuario)
            return True
        return False