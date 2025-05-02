class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["titulo"], data["autor"])