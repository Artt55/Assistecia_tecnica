import dbassitencia_tecnica as dba, viewassistencia as view

registro = dba.todos()
view.exibir_clientes(registro)
total_clientes = dba.contar()
total_resolvidos = dba.contar_resolvidos()
total_pendentes = dba.contar_pendentes()

print("------------------------------")
print(f"O total de clientes é...: {total_clientes}")
print(f"O total de clientes resolvidos é...: {total_resolvidos}")
print(f"O total de clientes pendentes é...: {total_pendentes}")