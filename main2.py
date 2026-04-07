# Função do menu de cadastro, arrumar dps para corresponder o que precisa dos requisitos
def menu_cadastro():
    while True:
        print("Menu de Cadasto:"
            "\n1- Cadastrar novo solicitante"
            "\n2- Editar solicitante"
            '\n0- Voltar')
        try: 
            selec = int(input("Digite sua escolha: "))
        except ValueError:
            print("Digite apenas números!")
        else:
            if selec > 2 or selec < 0:
                print("Digite uma opção válida!")
            elif selec == 1:
                print("Cadastro...")
                # Mudar para uma def quando essa parte estiver pronta
            elif selec == 2:
                print("Editar...")
                # Mudar para uma def quando essa parte estiver pronta
            elif selec == 0:
                print("Voltando...")
                break
            

# Função do menu de solicitação, arrumar dps para corresponder o que precisa dos requisitos
def menu_solicita():
    while True:
        print("Menu de Solicitação:"
            "\n1- Nova Solicitação"
            '\n0- Voltar')
        try: 
            selec = int(input("Digite sua escolha: "))
        except ValueError:
            print("Digite apenas números!")
        else:
            if selec > 1 or selec < 0:
                print("Digite uma opção válida!")
            elif selec == 1:
                print("Solicitação...")
                # Mudar para uma def quando essa parte estiver pronta  
            elif selec == 0:
                print("Voltando...")
                break



# Função do menu de consulta, arrumar dps para corresponder o que precisa dos requisitos
def menu_consulta():
    while True:
        print("Menu de Consulta: "
            "\n1- Consultar solicitações"
            "\n2- Atualizar solicitações"
            '\n0- Voltar')
        try: 
            selec = int(input("Digite sua escolha: "))
        except ValueError:
            print("Digite apenas números!")
        else:
            if selec > 2 or selec < 0:
                print("Digite uma opção válida!")
            elif selec == 1:
                print("Consulta...")
                # Mudar para uma def quando essa parte estiver pronta
            elif selec == 2:
                print("Atualizar...")
                # Mudar para uma def quando essa parte estiver pronta
            elif selec == 0:
                print("Voltando...")
                break



# Função do menu de estatiscas, arrumar dps para corresponder o que precisa dos requisitos
def menu_estatistica():
    while True:
        print("Menu de Estatíscas: "
            "\n1- Ver estatíscas"
            "\n2- Atualizar estatíscas"
            '\n0- Voltar')
        try: 
            selec = int(input("Digite sua escolha: "))
        except ValueError:
            print("Digite apenas números!")
        else:
            if selec > 2 or selec < 0:
                print("Digite uma opção válida!")
            elif selec == 1:
                print("Estatíscas...")
                # Mudar para uma def quando essa parte estiver pronta
            elif selec == 2:
                print("Atualizar...")
                # Mudar para uma def quando essa parte estiver pronta
            elif selec == 0:
                print("Voltando...")
                break




# Função do menu principal, ele refere o usuario para outras funções
# Não foi feito por IA, os comentários foram feitos por mim mesmo -Murilo
def menu_inicial():
    while True:
        print("Menu Principal: "
        "\n1-Cadastrar Solicitante"
        "\n2-Abrir Solicitação"
        "\n3-Consultar Solicitações"
        "\n4-Ver estatísticas"
        "\n0-Sair")
        try:
            selec = int(input("Digite sua escolha: "))
        except ValueError:
             print("Digite apenas números!")
        else:
            if selec > 4 or selec < 0:
                print("Selecione uma opção válida")
            elif selec == 1:
                menu_cadastro()
            elif selec == 2:
                menu_solicita()
            elif selec == 3:
                menu_cadastro()
            elif selec == 4:
                menu_estatistica()
            elif selec == 0:
                print("Saindo do programa...")
                break
     
     
            
# Não remova esse menu_inicial() do final, plmds
# Deixe ele sempre no final do código
menu_inicial()
        
import re

usuarios = []

def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email)

def cadastrar():
    print("=== Cadastro de Usuário ===")
    
    nome = input("Digite seu nome: ")
    if nome == "":
        print("Nome não pode ser vazio.")
        return
    
    email = input("Digite seu email: ")
    if not validar_email(email):
        print("Email inválido.")
        return
    
    senha = input("Digite sua senha (mínimo 6 caracteres): ")
    if len(senha) < 6:
        print("Senha muito curta.")
        return
    
    confirmar = input("Confirme sua senha: ")
    if senha != confirmar:
        print("As senhas não coincidem.")
        return
    
    usuario = {
        "nome": nome,
        "email": email,
        "senha": senha
    }
    
    usuarios.append(usuario)
    print("Cadastro realizado com sucesso!")

def listar():
    print("\n=== Usuários Cadastrados ===")
    for u in usuarios:
        print(f"Nome: {u['nome']} | Email: {u['email']}")

# Menu
while True:
    print("\n1 - Cadastrar")
    print("2 - Listar usuários")
    print("3 - Sair")
    
    opcao = input("Escolha: ")
    
    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
        #requisitos do cadastro pronto        
