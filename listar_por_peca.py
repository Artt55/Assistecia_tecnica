import dbassitencia_tecnica as dba, viewassistencia as view

peca_pesquisada = input("Digite o nome da peça: ")
resultado = dba.por_peca(peca_pesquisada)
if len(resultado) == 0:      
    print("Nenhum(a) cliente encontrado com a peça informada")
else:
    view.exibir_clientes(resultado)