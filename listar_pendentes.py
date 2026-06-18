import dbassitencia_tecnica as dba, viewassistencia as view

resultado = dba.pendentes()
view.exibir_clientes(resultado)
