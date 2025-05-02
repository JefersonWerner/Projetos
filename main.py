from sistema.biblioteca import Biblioteca

def main():
    biblioteca = Biblioteca()
    biblioteca.carregar_dados()
    biblioteca.inicializar_catalogo_se_vazio()

    while True:
        print("\n--- Sistema de Biblioteca Escolar ---")
        print("1 - Cadastrar Usuário")
        print("2 - Acessar como Usuário")
        print("3 - Ver Resumo dos Usuários")
        print("4 - Mostrar Arquivo JSON")
        print("5 - Salvar e Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            biblioteca.cadastrar_usuario()
        elif opcao == "2":
            biblioteca.menu_usuario()
        elif opcao == "3":
            biblioteca.resumo_usuarios()
        elif opcao == "4":
            biblioteca.mostrar_json()
        elif opcao == "5":
            biblioteca.salvar_dados()
            print("Dados salvos. Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()