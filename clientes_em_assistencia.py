import dbassitencia_tecnica as dba
import viewassistencia as view

registros = dba.todos()
view.exibir_clientes(registros)

print(f"Total de clientes: {dba.contar()}")
print(f"Total de clientes resolvidos: {dba.contar_resolvidos()}")
print(f"Total de clientes pendentes: {dba.contar_pendentes()}")