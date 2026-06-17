def exibir_clientes(registros):
    for registro in registros:
        nome, contato, email, problema_do_pc, pecas_trocadas, custo_peca, valor_servico, orcamento_final = registro.strip().split(",")
        print(f"Nome: {nome}")
        print(f"Contato: {contato}")
        print(f"E-mail: {email}")
        print(f"Problema do PC: {problema_do_pc}")
        print(f"Peça trocada: {pecas_trocadas}")
        print(f"Custo da peça: {custo_peca}")
        print(f"Valor do serviço: {valor_servico}")
        print(f"Orçamento final: {orcamento_final}")
        print("-" * 30)