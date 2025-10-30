Funcionarios = []

def cadastroFuncionario():
    print("\n--- Cadastro ---")
    Nome = input("Nome: ").strip()
    while True:
        try:
            Salario = float(input("Salário: "))
            break
        except ValueError:
            print("Salário inválido!")
    Funcionarios.append({'Nome': Nome, 'Salario': Salario})
    print(f"'{Nome}' cadastrado")

def listasFuncionario():
    print("\n--- Lista ---")
    if not Funcionarios:
        print("Nenhum funcionário")
        return
    for func in Funcionarios:
        print(f"Nome: {func['Nome']} | Salário: R$ {func['Salario']:.2f}")

def buscarFuncionario():
    if not Funcionarios:
        return print("Nenhum funcionário para buscar")
    
    Termo = input("Buscar Nome: ").lower()
    Encontrados = [f for f in Funcionarios if Termo in f['Nome'].lower()]
    
    if Encontrados:
        [print(f"- {f['Nome']} | R$ {f['Salario']:.2f}") for f in Encontrados]
    else:
        print("Não encontrado!")

def calculaMedSalario():
    print("\n--- Média Salarial ---")
    if not Funcionarios:
        print("Nenhum funcionário para calcular")
        return
    Soma = sum(func['Salario'] for func in Funcionarios)
    Media = Soma / len(Funcionarios)
    print(f"Média: R$ {Media:.2f}")

while True:
    print("\n--- Menu ---")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Buscar")
    print("4 - Média Salarial")
    print("5 - Sair")
    
    Opcao = input("Opção: ").strip()

    if Opcao == '1':
        cadastroFuncionario()
    elif Opcao == '2':
        listasFuncionario()
    elif Opcao == '3':
        buscarFuncionario()
    elif Opcao == '4':
        calculaMedSalario()
    elif Opcao == '5':
        print("Saindo")
        break
    else:

        print("Opção inválida")
