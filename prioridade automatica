import re
import mysql.connector
from mysql.connector import Error
from datetime import datetime

###
#  CONEXÃO
###


def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host='172.16.12.14',
            user='BD240226189',
            password='Dgqhx7',
            database='BD240226189'
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None


###
#  UTILITÁRIOS
###

def calcular_prioridade(urgencia, impacto):
    """
    Calcula a prioridade com base na urgência e no impacto.

    Matriz (ITIL):
              Impacto
              Baixo  Médio  Alto
    Urgência
    Baixa  →  Baixa  Baixa  Média
    Média  →  Baixa  Média  Alta
    Alta   →  Média  Alta   Alta
    """
    matriz = {
        ("Baixa", "Baixo"): "Baixa",
        ("Baixa", "Médio"): "Baixa",
        ("Baixa", "Alto"):  "Média",
        ("Média", "Baixo"): "Baixa",
        ("Média", "Médio"): "Média",
        ("Média", "Alto"):  "Alta",
        ("Alta",  "Baixo"): "Média",
        ("Alta",  "Médio"): "Alta",
        ("Alta",  "Alto"):  "Alta",
    }
    return matriz.get((urgencia, impacto), "Baixa")


def selecionar_urgencia():
    """Solicita ao usuário que escolha a urgência. Retorna a string ou None em caso de erro."""
    opcoes = {1: "Baixa", 2: "Média", 3: "Alta"}
    print("Urgência:")
    for k, v in opcoes.items():
        print(f"  {k}- {v}")
    try:
        sel = int(input("Escolha a urgência: "))
        urgencia = opcoes.get(sel)
        if not urgencia:
            print("Opção de urgência inválida.")
        return urgencia
    except ValueError:
        print("Entrada inválida para urgência.")
        return None


def selecionar_impacto():
    """Solicita ao usuário que escolha o impacto. Retorna a string ou None em caso de erro."""
    opcoes = {1: "Baixo", 2: "Médio", 3: "Alto"}
    print("Impacto:")
    for k, v in opcoes.items():
        print(f"  {k}- {v}")
    try:
        sel = int(input("Escolha o impacto: "))
        impacto = opcoes.get(sel)
        if not impacto:
            print("Opção de impacto inválida.")
        return impacto
    except ValueError:
        print("Entrada inválida para impacto.")
        return None


###
#  CRUD
###

def listar_solicitantes():
    """Exibe todos os solicitantes cadastrados."""
    print("\n── Listar Solicitantes ──")

    conn = criar_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cadastro_solicitantes ORDER BY codigo asc")
        rows = cursor.fetchall()

        if not rows:
            print("Nenhum solicitante cadastrado.")
            return

        print(f"\n{'Codigo':<8} {'Nome':<30} {'Email':<35} {'Telefone'}")
        print("─" * 80)
        for row in rows:
            # 0=codigo, 1=nome, 2=email, 3=telefone
            print(f"{row[0]:<8} {row[1]:<30} {row[2]:<35} {row[3]}")

    except Error as e:
        print(f"Erro ao listar solicitantes: {e}")
    finally:
        cursor.close()
        conn.close()


def cadastrar_solicitante():
    print("\n── Cadastrar Solicitante ──")
    nome     = input("Nome: ").strip()
    email    = input("Email (opcional): ").strip()
    telefone = input("Telefone (opcional, ex: (19) 99999-0000): ").strip()

    if not nome:
        print("Nome não pode ser vazio.")
        return
    if not email and not telefone:
        print("Informe ao menos um meio de contato (email ou telefone).")
        return
    if email and not validar_email(email):
        print("Email inválido. Use o formato: exemplo@dominio.com")
        return
    if telefone and not validar_telefone(telefone):
        print("Telefone inválido. Use o formato: (19) 99999-0000")
        return

    conn = criar_conexao()
    if not conn:
        return
    cursor = None
    try:
        cursor = conn.cursor()

        if email:
            cursor.execute("SELECT codigo FROM cadastro_solicitantes WHERE email = %s", (email,))
            if cursor.fetchone():
                print(f"Erro: o email '{email}' já está cadastrado.")
                return

        if telefone:
            cursor.execute("SELECT codigo FROM cadastro_solicitantes WHERE telefone = %s", (telefone,))
            if cursor.fetchone():
                print(f"Erro: o telefone '{telefone}' já está cadastrado.")
                return

        sql = "INSERT INTO cadastro_solicitantes (nome, email, telefone) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, email, telefone))
        conn.commit()
        print(f"Solicitante '{nome}' cadastrado com sucesso! (Codigo: {cursor.lastrowid})")
    except Error as e:
        print(f"Erro ao cadastrar solicitante: {e}")
    finally:
        if cursor:
            cursor.close()
        conn.close()

    
def validar_email(email):
    """Verifica se o email tem um formato válido."""
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(padrao, email) is not None

def validar_telefone(telefone):
    """Verifica se o telefone tem um formato válido. Ex: (19) 99999-0000"""
    padrao = r'^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$'
    return re.match(padrao, telefone) is not None

def editar_solicitante():
    """Atualiza os dados de um solicitante existente."""
    print("\n── Editar Solicitante ──")
    listar_solicitantes()

    try:
        codigo_editar = int(input("\nDigite o Codigo do solicitante a editar: "))
    except ValueError:
        print("Codigo inválido.")
        return

    conn = criar_conexao()
    if not conn:
        return
    cursor = None
    try:
        cursor = conn.cursor()

        # Busca os dados atuais do solicitante
        cursor.execute("SELECT * FROM cadastro_solicitantes WHERE codigo = %s", (codigo_editar,))
        solicitante = cursor.fetchone()
        if not solicitante:
            print("Solicitante não encontrado.")
            return

        # 0=codigo, 1=nome, 2=email, 3=telefone
        print(f"\nDados atuais → Nome: {solicitante[1]} | Email: {solicitante[2]} | Telefone: {solicitante[3]}")
        print("(Pressione Enter para manter o valor atual)")

        novo_nome     = input(f"Novo nome [{solicitante[1]}]: ").strip() or solicitante[1]
        novo_email    = input(f"Novo email [{solicitante[2]}]: ").strip() or solicitante[2]
        novo_telefone = input(f"Novo telefone [{solicitante[3]}]: ").strip() or solicitante[3]

        if not novo_nome:
            print("Nome não pode ser vazio.")
            return
        if not novo_email and not novo_telefone:
            print("Informe ao menos um meio de contato (email ou telefone).")
            return
        if novo_email and not validar_email(novo_email):
            print("Email inválido. Use o formato: exemplo@dominio.com")
            return
        if novo_telefone and not validar_telefone(novo_telefone):
            print("Telefone inválido. Use o formato: (19) 99999-0000")
            return

        # Verifica duplicidade ignorando o próprio registro
        if novo_email:
            cursor.execute(
                "SELECT codigo FROM cadastro_solicitantes WHERE email = %s AND codigo != %s",
                (novo_email, codigo_editar)
            )
            if cursor.fetchone():
                print(f"Erro: o email '{novo_email}' já está cadastrado.")
                return

        if novo_telefone:
            cursor.execute(
                "SELECT codigo FROM cadastro_solicitantes WHERE telefone = %s AND codigo != %s",
                (novo_telefone, codigo_editar)
            )
            if cursor.fetchone():
                print(f"Erro: o telefone '{novo_telefone}' já está cadastrado.")
                return

        sql = "UPDATE cadastro_solicitantes SET nome=%s, email=%s, telefone=%s WHERE codigo=%s"
        cursor.execute(sql, (novo_nome, novo_email, novo_telefone, codigo_editar))
        conn.commit()
        print("Solicitante atualizado com sucesso!")
    except Error as e:
        print(f"Erro ao editar solicitante: {e}")
    finally:
        if cursor:
            cursor.close()
        conn.close()


def excluir_solicitante():
    """Remove um solicitante do banco de dados."""
    print("\n── Excluir Solicitante ──")
    listar_solicitantes()

    try:
        codigo_excluir = int(input("\nDigite o Codigo do solicitante a excluir: "))
    except ValueError:
        print("Codigo inválido.")
        return

    confirmacao = input(f"Confirma exclusão do Codigo {codigo_excluir}? (s/n): ").strip().lower()
    if confirmacao != 's':
        print("Exclusão cancelada.")
        return

    conn = criar_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cadastro_solicitantes WHERE codigo = %s", (codigo_excluir,))
        conn.commit()
        if cursor.rowcount:
            print("Solicitante excluído com sucesso!")
        else:
            print("Solicitante não encontrado.")
    except Error as e:
        print(f"Erro ao excluir solicitante: {e}")
    finally:
        cursor.close()
        conn.close()


def listar_categorias():
    """Exibe todas as categorias disponíveis."""
    conn = criar_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM categorias")
        rows = cursor.fetchall()
        if not rows:
            print("Nenhuma categoria cadastrada.")
            return
        print(f"\n{'ID':<6} {'Categoria'}")
        print("─" * 40)
        for row in rows:
            print(f"{row[0]:<6} {row[1]}")
    except Error as e:
        print(f"Erro ao listar categorias: {e}")
    finally:
        cursor.close()
        conn.close()


def nova_solicitacao():
    """Cria uma nova solicitação vinculada a um solicitante."""
    print("\n── Nova Solicitação ──")
    listar_solicitantes()

    try:
        codigo_solicitante = int(input("\nDigite o Codigo do solicitante: "))
    except ValueError:
        print("Codigo inválido.")
        return

    descricao = input("Descrição da solicitação: ").strip()
    if not descricao:
        print("Descrição não pode ser vazia.")
        return

    print("\nCategorias disponíveis:")
    listar_categorias()

    try:
        id_categoria = int(input("\nID da categoria: "))
    except ValueError:
        print("ID de categoria inválido.")
        return

    # Coleta urgência e impacto; calcula a prioridade automaticamente
    print()
    urgencia = selecionar_urgencia()
    if not urgencia:
        return

    print()
    impacto = selecionar_impacto()
    if not impacto:
        return

    prioridade = calcular_prioridade(urgencia, impacto)
    print(f"\nPrioridade calculada automaticamente: {prioridade}")

    conn = criar_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()

        cursor.execute("SELECT codigo FROM cadastro_solicitantes WHERE codigo = %s", (codigo_solicitante,))
        if not cursor.fetchone():
            print("Solicitante não encontrado.")
            return

        cursor.execute("SELECT id FROM categorias WHERE id = %s", (id_categoria,))
        if not cursor.fetchone():
            print("Categoria não encontrada.")
            return

        sql = """INSERT INTO solicitacoes
                    (codigo_solicitante, id_categoria, descricao, data_abertura,
                     status, urgencia, impacto, prioridade)
                 VALUES (%s, %s, %s, %s, 'Aberta', %s, %s, %s)"""
        cursor.execute(sql, (
            codigo_solicitante, id_categoria, descricao,
            datetime.now(), urgencia, impacto, prioridade
        ))
        conn.commit()
        print(f"Solicitação aberta com sucesso! (ID: {cursor.lastrowid})")
    except Error as e:
        print(f"Erro ao criar solicitação: {e}")
    finally:
        cursor.close()
        conn.close()


def consultar_solicitacoes():
    """Exibe todas as solicitações com nome do solicitante."""
    print("\n── Consultar Solicitações ──")
    conn = criar_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        sql = """SELECT s.id, s.codigo_solicitante, cs.nome, s.id_categoria,
                        s.descricao, s.data_abertura, s.status,
                        s.urgencia, s.impacto, s.prioridade
                 FROM solicitacoes s
                 JOIN cadastro_solicitantes cs ON s.codigo_solicitante = cs.codigo
                 ORDER BY s.data_abertura DESC"""
        cursor.execute(sql)
        rows = cursor.fetchall()
        if not rows:
            print("Nenhuma solicitação encontrada.")
            return
        print(f"\n{'ID':<6} {'Cód.':<6} {'Solicitante':<22} {'Cat':<5} {'Status':<15} "
              f"{'Urgência':<10} {'Impacto':<9} {'Prioridade':<11} {'Abertura':<18} Descrição")
        print("─" * 130)
        for r in rows:
            # 0=id,1=cod,2=nome,3=cat,4=desc,5=data,6=status,7=urgencia,8=impacto,9=prioridade
            data = r[5].strftime('%d/%m/%Y %H:%M') if r[5] else '-'
            print(f"{r[0]:<6} {r[1]:<6} {r[2]:<22} {r[3]:<5} {r[6]:<15} "
                  f"{r[7]:<10} {r[8]:<9} {r[9]:<11} {data:<18} {r[4]}")
    except Error as e:
        print(f"Erro ao consultar solicitações: {e}")
    finally:
        cursor.close()
        conn.close()

            
def consultar_solicitacoes_filtro():
    """Consulta solicitações com filtros opcionais."""
    print("\n── Filtrar Solicitações ──")
    print("(Pressione Enter para ignorar o filtro)")

    print("\nUrgência: Baixa | Média | Alta")
    filtro_urgencia = input("Filtrar por urgência: ").strip() or None

    print("Impacto: Baixo | Médio | Alto")
    filtro_impacto = input("Filtrar por impacto: ").strip() or None

    print("Prioridade (calculada): Baixa | Média | Alta")
    filtro_prioridade = input("Filtrar por prioridade: ").strip() or None

    print("Status: Aberta | Em andamento | Fechada")
    filtro_status = input("Filtrar por status: ").strip() or None

    print("\nCategorias disponíveis:")
    listar_categorias()
    filtro_categoria = input("Filtrar por ID de categoria (número): ").strip() or None

    print("\nSolicitantes disponíveis:")
    listar_solicitantes()
    filtro_solicitante = input("Filtrar por código do solicitante (número): ").strip() or None

    conn = criar_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()

        sql = """SELECT s.id, s.codigo_solicitante, cs.nome, s.id_categoria,
                        s.descricao, s.data_abertura, s.status,
                        s.urgencia, s.impacto, s.prioridade
                 FROM solicitacoes s
                 JOIN cadastro_solicitantes cs ON s.codigo_solicitante = cs.codigo
                 WHERE 1=1"""

        parametros = []

        if filtro_urgencia:
            sql += " AND s.urgencia = %s"
            parametros.append(filtro_urgencia)

        if filtro_impacto:
            sql += " AND s.impacto = %s"
            parametros.append(filtro_impacto)

        if filtro_prioridade:
            sql += " AND s.prioridade = %s"
            parametros.append(filtro_prioridade)

        if filtro_status:
            sql += " AND s.status = %s"
            parametros.append(filtro_status)

        if filtro_categoria:
            sql += " AND s.id_categoria = %s"
            parametros.append(filtro_categoria)

        if filtro_solicitante:
            sql += " AND s.codigo_solicitante = %s"
            parametros.append(filtro_solicitante)

        sql += " ORDER BY s.data_abertura DESC"

        cursor.execute(sql, parametros)
        rows = cursor.fetchall()

        if not rows:
            print("Nenhuma solicitação encontrada com esses filtros.")
            return

        print(f"\n{'ID':<6} {'Cód.':<6} {'Solicitante':<22} {'Cat':<5} {'Status':<15} "
              f"{'Urgência':<10} {'Impacto':<9} {'Prioridade':<11} {'Abertura':<18} Descrição")
        print("─" * 130)
        for r in rows:
            data = r[5].strftime('%d/%m/%Y %H:%M') if r[5] else '-'
            print(f"{r[0]:<6} {r[1]:<6} {r[2]:<22} {r[3]:<5} {r[6]:<15} "
                  f"{r[7]:<10} {r[8]:<9} {r[9]:<11} {data:<18} {r[4]}")

    except Error as e:
        print(f"Erro ao filtrar solicitações: {e}")
    finally:
        cursor.close()
        conn.close()


def atualizar_solicitacao():
    """Atualiza descrição, status, urgência e/ou impacto de uma solicitação.
       A prioridade é recalculada automaticamente."""
    print("\n── Atualizar Solicitação ──")
    consultar_solicitacoes()

    try:
        id_sol = int(input("\nDigite o ID da solicitação a atualizar: "))
    except ValueError:
        print("ID inválido.")
        return

    conn = criar_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM solicitacoes WHERE id = %s", (id_sol,))
        sol = cursor.fetchone()
        if not sol:
            print("Solicitação não encontrada.")
            return

        # Índices esperados:
        # 0=id, 1=codigo_solicitante, 2=id_categoria, 3=descricao,
        # 4=data_abertura, 5=status, 6=urgencia, 7=impacto, 8=prioridade

        opcoes_status = {1: "Aberta", 2: "Em andamento", 3: "Fechada"}
        opcoes_urg    = {1: "Baixa",  2: "Média",        3: "Alta"}
        opcoes_imp    = {1: "Baixo",  2: "Médio",        3: "Alto"}

        # Status
        print(f"\nStatus atual: {sol[5]}")
        print("  1- Aberta  2- Em andamento  3- Fechada")
        try:
            sel_status = int(input("Novo status (Enter para manter): ") or 0)
            novo_status = opcoes_status.get(sel_status, sol[5])
        except ValueError:
            novo_status = sol[5]

        # Descrição
        nova_desc = input(f"\nNova descrição [{sol[3]}]: ").strip() or sol[3]

        # Urgência
        print(f"\nUrgência atual: {sol[6]}")
        print("  1- Baixa  2- Média  3- Alta")
        try:
            sel_urg = int(input("Nova urgência (Enter para manter): ") or 0)
            nova_urgencia = opcoes_urg.get(sel_urg, sol[6])
        except ValueError:
            nova_urgencia = sol[6]

        # Impacto
        print(f"\nImpacto atual: {sol[7]}")
        print("  1- Baixo  2- Médio  3- Alto")
        try:
            sel_imp = int(input("Novo impacto (Enter para manter): ") or 0)
            novo_impacto = opcoes_imp.get(sel_imp, sol[7])
        except ValueError:
            novo_impacto = sol[7]

        # Recalcula prioridade
        nova_prioridade = calcular_prioridade(nova_urgencia, novo_impacto)
        print(f"\nPrioridade recalculada automaticamente: {nova_prioridade}")

        sql = """UPDATE solicitacoes
                 SET status=%s, descricao=%s, urgencia=%s, impacto=%s, prioridade=%s
                 WHERE id=%s"""
        cursor.execute(sql, (novo_status, nova_desc, nova_urgencia, novo_impacto, nova_prioridade, id_sol))
        conn.commit()
        print(f"Solicitação atualizada! Status: {novo_status} | Urgência: {nova_urgencia} | "
              f"Impacto: {novo_impacto} | Prioridade: {nova_prioridade}")
    except Error as e:
        print(f"Erro ao atualizar solicitação: {e}")
    finally:
        cursor.close()
        conn.close()


def excluir_solicitacao():
    """Remove uma solicitação do banco de dados."""
    print("\n── Excluir Solicitação ──")
    consultar_solicitacoes()

    try:
        id_sol = int(input("\nDigite o ID da solicitação a excluir: "))
    except ValueError:
        print("ID inválido.")
        return

    confirmacao = input(f"Confirma exclusão da solicitação {id_sol}? (s/n): ").strip().lower()
    if confirmacao != 's':
        print("Exclusão cancelada.")
        return

    conn = criar_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM solicitacoes WHERE id = %s", (id_sol,))
        conn.commit()
        if cursor.rowcount:
            print("Solicitação excluída com sucesso!")
        else:
            print("Solicitação não encontrada.")
    except Error as e:
        print(f"Erro ao excluir solicitação: {e}")
    finally:
        cursor.close()
        conn.close()
        
###
#  ESTATÍSTICAS
###

def ver_estatisticas():
    """Exibe um resumo estatístico das solicitações."""
    print("\n── Estatísticas ──")
    conn = criar_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM cadastro_solicitantes")
        total_solic = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM solicitacoes")
        total_req = cursor.fetchone()[0]

        cursor.execute("SELECT status, COUNT(*) FROM solicitacoes GROUP BY status")
        por_status = cursor.fetchall()

        cursor.execute("SELECT urgencia, COUNT(*) FROM solicitacoes GROUP BY urgencia")
        por_urgencia = cursor.fetchall()

        cursor.execute("SELECT impacto, COUNT(*) FROM solicitacoes GROUP BY impacto")
        por_impacto = cursor.fetchall()

        cursor.execute("SELECT prioridade, COUNT(*) FROM solicitacoes GROUP BY prioridade")
        por_prioridade = cursor.fetchall()

        cursor.execute("""
            SELECT cs.nome, COUNT(s.id) AS qtd
            FROM solicitacoes s
            JOIN cadastro_solicitantes cs ON s.codigo_solicitante = cs.codigo
            GROUP BY cs.nome ORDER BY qtd DESC LIMIT 5
        """)
        top_solic = cursor.fetchall()

        print(f"\nTotal de solicitantes cadastrados : {total_solic}")
        print(f"Total de solicitações             : {total_req}")

        print("\nSolicitações por status:")
        for row in por_status:
            print(f"  {row[0]:<20}: {row[1]}")

        print("\nSolicitações por urgência:")
        for row in por_urgencia:
            print(f"  {row[0]:<20}: {row[1]}")

        print("\nSolicitações por impacto:")
        for row in por_impacto:
            print(f"  {row[0]:<20}: {row[1]}")

        print("\nSolicitações por prioridade (calculada):")
        for row in por_prioridade:
            print(f"  {row[0]:<20}: {row[1]}")

        if top_solic:
            print("\nTop 5 solicitantes com mais solicitações:")
            for i, row in enumerate(top_solic, 1):
                print(f"  {i}. {row[0]} – {row[1]} solicitação(ões)")

    except Error as e:
        print(f"Erro ao gerar estatísticas: {e}")
    finally:
        cursor.close()
        conn.close()


###
#  MENUS
###

def menu_cadastro():
    opcoes = {
        1: ("Cadastrar novo solicitante", cadastrar_solicitante),
        2: ("Listar solicitantes",        listar_solicitantes),
        3: ("Editar solicitante",         editar_solicitante),
        4: ("Excluir solicitante",        excluir_solicitante),
    }
    while True:
        print("\n── Menu de Cadastro ──")
        for k, (desc, _) in opcoes.items():
            print(f"{k}- {desc}")
        print("0- Voltar")
        try:
            selec = int(input("Escolha: "))
        except ValueError:
            print("Digite apenas números!")
            continue
        if selec == 0:
            break
        elif selec in opcoes:
            opcoes[selec][1]()
        else:
            print("Opção inválida!")


def menu_solicita():
    opcoes = {
        1: ("Nova solicitação",     nova_solicitacao),
        2: ("Excluir solicitação",  excluir_solicitacao),
    }
    while True:
        print("\n── Menu de Solicitação ──")
        for k, (desc, _) in opcoes.items():
            print(f"{k}- {desc}")
        print("0- Voltar")
        try:
            selec = int(input("Escolha: "))
        except ValueError:
            print("Digite apenas números!")
            continue
        if selec == 0:
            break
        elif selec in opcoes:
            opcoes[selec][1]()
        else:
            print("Opção inválida!")


def menu_consulta():
    opcoes = {
        1: ("Consultar solicitações",          consultar_solicitacoes),
        2: ("Consultar com filtros",           consultar_solicitacoes_filtro),
        3: ("Atualizar solicitação",           atualizar_solicitacao),
    }
    while True:
        print("\n── Menu de Consulta ──")
        for k, (desc, _) in opcoes.items():
            print(f"{k}- {desc}")
        print("0- Voltar")
        try:
            selec = int(input("Escolha: "))
        except ValueError:
            print("Digite apenas números!")
            continue
        if selec == 0:
            break
        elif selec in opcoes:
            opcoes[selec][1]()
        else:
            print("Opção inválida!")

def menu_estatistica():
    opcoes = {
        1: ("Ver estatísticas", ver_estatisticas),
    }
    while True:
        print("\n── Menu de Estatísticas ──")
        for k, (desc, _) in opcoes.items():
            print(f"{k}- {desc}")
        print("0- Voltar")
        try:
            selec = int(input("Escolha: "))
        except ValueError:
            print("Digite apenas números!")
            continue
        if selec == 0:
            break
        elif selec in opcoes:
            opcoes[selec][1]()
        else:
            print("Opção inválida!")


def menu_inicial():
    print("\nTestando conexão...")
    conn = criar_conexao()
    if conn and conn.is_connected():
        print("Conexão estabelecida com sucesso!")
        conn.close()
    else:
        print("AVISO: Falha na conexão. Verifique as credenciais do banco.")

    while True:
        print("\n══ Menu Principal ══"
              "\n1- Cadastrar Solicitante"
              "\n2- Abrir Solicitação"
              "\n3- Consultar Solicitações"
              "\n4- Ver Estatísticas"
              "\n0- Sair")
        try:
            selec = int(input("Digite sua escolha: "))
        except ValueError:
            print("Digite apenas números!")
            continue

        if selec == 1:
            menu_cadastro()
        elif selec == 2:
            menu_solicita()
        elif selec == 3:
            menu_consulta()
        elif selec == 4:
            menu_estatistica()
        elif selec == 0:
            print("Saindo do programa...")
            break
        else:
            print("Selecione uma opção válida.")


# Não remova esse menu_inicial() do final, plmds
# Deixe ele sempre no final do código
menu_inicial()
