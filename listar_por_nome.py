import dbassitencia_tecnica as dba, viewassistencia as view

nome_pesquisado = input("Digite o nome completo do cliente: ")
resultado = dba.por_nome(nome_pesquisado)
if len(resultado) == 0:      
    print("Nenhum(a) cliente encontrado com o nome informado")
else:
    view.exibir_clientes(resultado)
