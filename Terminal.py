print("Menu Principal\n1-Cadastrar Solicitante\n2-Abrir Solicitação\n3-Consultar Solicitações\n4-Ver estatísticas\n0-Sair")
def Menu():
    try:
        selec = int(input("Digite sua escolha: "))
    except ValueError:
         print("Digite apenas números!")
         Menu()
    else:
        if selec > 4 or selec < 0:
            print("Selecione uma opção válida")
            Menu()
        if selec == 1:
            print("Menu de cadastro")
            Menu()
        if selec == 2:
            print('Menu de solicitação')
            Menu()
        if selec == 3:
            print('Menu de consulta')
            Menu()
        if selec == 4:
            print('Menu de estatisca')
            Menu()
        if selec == 0:
            exit()
        

Menu()