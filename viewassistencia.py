def exibir_clientes(registros):
    for registro in registros:
        nome, telefone, email, problema_do_pc, pecas_trocadas, custo_peca, valor_servico, valor_total, status = registro.strip().split(",")
        print(f"Nome: {nome}")
        print(f"Contato: {telefone}")
        print(f"E-mail: {email}")
        print(f"Problema do PC: {problema_do_pc}")
        print(f"Peça trocada: {pecas_trocadas}")
        print(f"Custo da peça: R$ {float(custo_peca):.2f}")
        print(f"Valor do serviço: R$ {float(valor_servico):.2f}")
        print(f"Orçamento final: R$ {float(valor_total):.2f}")
        print(f"Status da situação: {status}")
        print("-" * 30)