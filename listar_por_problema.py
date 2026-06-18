import dbassitencia_tecnica as dba, viewassistencia as view

problema_pesquisado = input("Digite o problema do PC do cliente: ")
resultado = dba.por_problema(problema_pesquisado)
view.exibir_clientes(resultado)
