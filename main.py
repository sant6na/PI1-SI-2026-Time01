import mysql.connector
from mysql.connector import Error

# Conectar ao banco de dados
def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host='BD-ACD',
            user='BD240226189',      
            password='Dgqhx7',      
            database='BD240226189'
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None



print("Testando conexão")
teste_conn = criar_conexao()
if teste_conn and teste_conn.is_connected():
    print("Conexão estabelecida")
    teste_conn.close() 
else:
    print("Falha na conexão")





# Função do menu de cadastro, arrumar dps para corresponder o que precisa dos requisitos
def menu_cadastro():
    while True:
        print("Menu de Cadasto:"
            "\n1- Cadastrar novo solicitante"
            "\n2- Editar solicitante"
            "\n0- Voltar")
        try: 
            selec = int(input("Digite sua escolha: "))
        except ValueError:
            print("Digite apenas números!")
        else:
            if selec > 2 or selec < 0:
                print("Digite uma opção válida!")
            elif selec == 1:
                # função para fazer o cadastro de solicitante
                print("Cadastro...")
                nome = input("Digite o nome: ")
                email = input("Digite o email: ")
                telefone1 = input("Digite o telefone: ")
                
                conn = criar_conexao()
                if conn:
                    try:
                        cursor = conn.cursor()
                        sql = "INSERT INTO cadastro_solicitantes (nome, email, telefone) VALUES (%s, %s, %s)"
                        cursor.execute(sql, (nome, email, telefone1))
                        conn.commit()
                        print("Solicitante cadastrado com sucesso!")
                    except Error as e:
                        print(f"Erro ao cadastrar: {e}")
                    finally:
                        cursor.close()
                        conn.close()


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
            "\n0- Voltar")
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
            "\n0- Voltar")
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
            "\n0- Voltar")
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
                menu_consulta() # Ajustado para chamar a def de consulta correta
            elif selec == 4:
                menu_estatistica()
            elif selec == 0:
                print("Saindo do programa...")
                break
      
      
            
# Não remova esse menu_inicial() do final, plmds
# Deixe ele sempre no final do código
menu_inicial()

# teste de git