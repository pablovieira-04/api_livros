from app.models.usuario_model import Usuario
from app.dao.usuario_dao import UsuarioDAO
from typing import List

class UsuarioService:
    def __init__(self, dao: UsuarioDAO):
        self.dao = dao

    def listar_usuarios(self):
        return self.dao.listar_usuarios()

    def buscar_usuario_por_id(self, usuario_id: int):
        return self.dao.buscar_por_id(usuario_id)

    def adicionar_usuario(self, usuario: Usuario):
        return self.dao.adicionar_usuario(usuario)

    def atualizar_usuario(self, usuario_id: int, usuario: Usuario):
        return self.dao.atualizar_usuario(usuario_id, usuario)

    def deletar_usuario(self, usuario_id: int):
        return self.dao.deletar_usuario(usuario_id)
