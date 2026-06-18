import dbassitencia_tecnica as dba, viewassistencia as view

nome_pesquisado = input("Digite o nome completo do cliente: ")
resultado = dba.por_nome(nome_pesquisado)
view.exibir_clientes(resultado)
