import dbassitencia_tecnica as dba, viewassistencia as view

problema_pesquisado = input("Digite o problema do PC do cliente: ")
resultado = dba.por_problema(problema_pesquisado)
if len(resultado) == 0:      
    print("Nenhum(a) cliente encontrado com o problema informado")
else:
    view.exibir_clientes(resultado)
