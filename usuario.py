from .pessoa import Pessoa

class Usuario(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
        self.emprestimos = []

    def listar_emprestimos(self):
        print(f"\nEmpréstimos de {self.nome}:")
        for emprestimo in self.emprestimos:
            print(emprestimo)

    def to_dict(self):
        return {
            "nome": self.nome,
            "cpf": self.cpf,
            "emprestimos": [e.to_dict() for e in self.emprestimos]
        }

    @classmethod
    def from_dict(cls, data):
        user = cls(data["nome"], data["cpf"])
        return user