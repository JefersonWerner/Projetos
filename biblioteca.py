from .usuario import Usuario
from .livro import Livro
from .emprestimo import Emprestimo
from .persistencia import salvar_json, carregar_json

class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.catalogo = []
        self.emprestimos = []

    def carregar_dados(self):
        dados = carregar_json()
        self.usuarios = [Usuario.from_dict(u) for u in dados.get("usuarios", [])]
        self.catalogo = [Livro.from_dict(l) for l in dados.get("livros", [])]
        self.emprestimos = [Emprestimo.from_dict(e) for e in dados.get("emprestimos", [])]

    def salvar_dados(self):
        dados = {
            "usuarios": [u.to_dict() for u in self.usuarios],
            "livros": [l.to_dict() for l in self.catalogo],
            "emprestimos": [e.to_dict() for e in self.emprestimos]
        }
        salvar_json(dados)

    def inicializar_catalogo_se_vazio(self):
        if not self.catalogo:
            self.catalogo.append(Livro("1984", "George Orwell"))
            self.catalogo.append(Livro("Dom Casmurro", "Machado de Assis"))

    def cadastrar_usuario(self):
        nome = input("Nome do usuário: ")
        cpf = input("CPF: ")
        usuario = Usuario(nome, cpf)
        self.usuarios.append(usuario)
        print("Usuário cadastrado com sucesso.")

    def menu_usuario(self):
        cpf = input("Digite seu CPF: ")
        usuario = next((u for u in self.usuarios if u.cpf == cpf), None)
        if not usuario:
            print("Usuário não encontrado.")
            return

        while True:
            print(f"\nBem-vindo, {usuario.nome}")
            print("1 - Ver catálogo")
            print("2 - Realizar empréstimo")
            print("3 - Devolver livro")
            print("4 - Ver empréstimos")
            print("5 - Voltar")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.mostrar_catalogo()
            elif opcao == "2":
                self.realizar_emprestimo(usuario)
            elif opcao == "3":
                self.devolver_livro(usuario)
            elif opcao == "4":
                usuario.listar_emprestimos()
            elif opcao == "5":
                break

    def mostrar_catalogo(self):
        print("\n--- Catálogo de Livros ---")
        for livro in self.catalogo:
            print(livro)

    def realizar_emprestimo(self, usuario):
        self.mostrar_catalogo()
        titulo = input("Digite o título do livro: ")
        livro = next((l for l in self.catalogo if l.titulo == titulo), None)
        if not livro:
            print("Livro não encontrado.")
            return
        emprestimo = Emprestimo(usuario, livro)
        self.emprestimos.append(emprestimo)
        usuario.emprestimos.append(emprestimo)
        print("Empréstimo realizado.")

    def devolver_livro(self, usuario):
        usuario.listar_emprestimos()
        titulo = input("Digite o título do livro a devolver: ")
        emprestimo = next((e for e in usuario.emprestimos if e.livro.titulo == titulo), None)
        if not emprestimo:
            print("Empréstimo não encontrado.")
            return
        usuario.emprestimos.remove(emprestimo)
        self.emprestimos.remove(emprestimo)
        print("Livro devolvido com sucesso.")

    def resumo_usuarios(self):
        print("\n--- Usuários e Empréstimos ---")
        for u in self.usuarios:
            print(u)
            u.listar_emprestimos()

    def mostrar_json(self):
        import json
        dados = carregar_json()
        print(json.dumps(dados, indent=2, ensure_ascii=False))