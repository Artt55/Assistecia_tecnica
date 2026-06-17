def todos():
    clientes_assistencia = open(
        file="clientes_assistencia.csv",
        mode="r",
        encoding="utf-8"
    )
    registro = clientes_assistencia.readlines()
    clientes_assistencia.close()
    return registro

def por_nome(nome_pesquisado):
    registros = todos()
    registros_filtrados = list()
    for registro in registros:
        nome, contato, email, problema_do_pc, pecas_trocadas, custo_peca, valor_servico, orcamento_final = registro.strip().split(",")
        if nome == nome_pesquisado:
            registros_filtrados.append(registro)
    return registros_filtrados

def por_problema(problema_pesquisado):
    registros = todos()
    registros_filtrados = list()
    for registro in registros:
        nome, contato, email, problema_do_pc, pecas_trocadas, custo_peca, valor_servico, orcamento_final = registro.strip().split(",")
        if problema_do_pc == problema_pesquisado:
            registros_filtrados.append(registro)
    return registros_filtrados

def por_peca(peca_pesquisada):
    registros = todos()
    registros_filtrados = list()
    for registro in registros:
        nome, contato, email, problema_do_pc, pecas_trocadas, custo_peca, valor_servico, orcamento_final = registro.strip().split(",")
        if pecas_trocadas == peca_pesquisada:
            registros_filtrados.append(registro)
    return registros_filtrados

def pendentes():
    registros = todos()
    registros_filtrados = list()
    for registro in registros:
        nome, contato, email, problema_do_pc, pecas_trocadas, custo_peca, valor_servico, orcamento_final, status = registro.strip().split(",")
        if status == "Pendente":
            registros_filtrados.append(registro)
    return registros_filtrados

def resolvidos():
    registros = todos()
    registros_filtrados = list()
    for registro in registros:
        nome, contato, email, problema_do_pc, pecas_trocadas, custo_peca, valor_servico, orcamento_final, status = registro.strip().split(",")
        if status == "Resolvido":
            registros_filtrados.append(registro)
    return registros_filtrados

def contar_pendentes():
    return len(pendentes())

def contar_resolvidos():
    return len(resolvidos())

def problema_mais_frequente():
    registros = todos()
    contagem = {}
    for registro in registros:
        nome, contato, email, problema_do_pc, pecas_trocadas, custo_peca, valor_servico, orcamento_final, status = registro.strip().split(",")
        if problema_do_pc in contagem:
            contagem[problema_do_pc] += 1
        else:
            contagem[problema_do_pc] = 1
    return max(contagem, key=contagem.get)

def problema_menos_frequente():
    registros = todos()
    contagem = {}
    for registro in registros:
        nome, contato, email, problema_do_pc, pecas_trocadas, custo_peca, valor_servico, orcamento_final, status = registro.strip().split(",")
        if problema_do_pc in contagem:
            contagem[problema_do_pc] += 1
        else:
            contagem[problema_do_pc] = 1
    return min(contagem, key=contagem.get)

def maior_valor_gasto():
    registros = todos()
    maior = 0
    cliente_maior = ""
    for registro in registros:
        nome, contato, email, problema_do_pc, pecas_trocadas, custo_peca, valor_servico, orcamento_final, status = registro.strip().split(",")
        if float(orcamento_final) > maior:
            maior = float(orcamento_final)
            cliente_maior = nome
    return cliente_maior, maior

def menor_valor_gasto():
    registros = todos()
    menor = float("inf")
    cliente_menor = ""
    for registro in registros:
        nome, contato, email, problema_do_pc, pecas_trocadas, custo_peca, valor_servico, orcamento_final, status = registro.strip().split(",")
        if float(orcamento_final) < menor:
            menor = float(orcamento_final)
            cliente_menor = nome
    return cliente_menor, menor

def media_de_valor():
    registros = todos()
    total = 0
    for registro in registros:
        nome, contato, email, problema_do_pc, pecas_trocadas, custo_peca, valor_servico, orcamento_final, status = registro.strip().split(",")
        total += float(orcamento_final)
    return total / len(registros)

def contar():
    registros = todos()
    return len(registros)