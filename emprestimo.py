class Emprestimo:
    def __init__(self, usuario, livro):
        self.usuario = usuario
        self.livro = livro

    def __str__(self):
        return f"{self.livro.titulo} emprestado para {self.usuario.nome}"

    def to_dict(self):
        return {
            "usuario": self.usuario.nome,
            "livro": self.livro.to_dict()
        }

    @classmethod
    def from_dict(cls, data):
        from .livro import Livro
        return cls(usuario=None, livro=Livro.from_dict(data["livro"]))