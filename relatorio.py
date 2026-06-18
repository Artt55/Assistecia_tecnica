import dbassitencia_tecnica as dba

print(f"Esse é o problema mais frequente...: {dba.problema_mais_frequente()}")
print(f"Esse é o problema menos frequente...: {dba.problema_menos_frequente()}")
print(f"Esse é o problema mais frequente entre os clientes resolvidos...: {dba.problema_mais_frequente_resolvidos()}")
print(f"Esse é o problema mais frequente entre os clientes pendentes...: {dba.problema_mais_frequente_pendentes()}")
print(f"Esse é o problema menos frequente entre os clientes resolvidos...: {dba.problema_menos_frequente_resolvidos()}")
print(f"Esse é o problema menos frequente entre os clientes pendentes...: {dba.problema_menos_frequente_pendentes()}")
cliente, valor = dba.maior_valor_gasto()
print(f"Esse é o maior valor gasto por um cliente...: {cliente} - R$ {valor:.2f}")
cliente, valor = dba.menor_valor_gasto()
print(f"Esse é o menor valor gasto por um cliente...: {cliente} - R$ {valor:.2f}")
print(f"Essa é a média de valor gasto por cliente...: R${dba.media_de_valor():.2f}")