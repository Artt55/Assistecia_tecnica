import dbassitencia_tecnica as dba

nome = input("Nome do cliente: ")
telefone = input("Telefone: ")
email = input("Email: ")
problema_do_pc = input("Problema do PC: ")
pecas_trocadas = input("Peças trocadas: ")
custo_peca = float(input("Custo da peça: "))
valor_servico = float(input("Valor do serviço: "))
valor_total = float(input("Valor total: "))
status = input("Status (Pendente/Resolvido): ")

dba.cadastrar(nome, telefone, email, problema_do_pc, pecas_trocadas, custo_peca, valor_servico, valor_total, status)
print("Cliente cadastrado com sucesso!")
