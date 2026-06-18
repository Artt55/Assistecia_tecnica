# Projeto Integrador 2026 - SENAC Tech
## Porjeto - Assistência Técnica

### Dados
- Nome do cliente
- Telefone
- Email
- Problema do PC 
- Pecas Trocadas 
- Valor das Pecas (R$) 
- Valor do Servico (R$) 
- Valor total (R$)
- Valor medio gasto
- Maior valor
- Menor valor
- Problema mais frequente
- Problema menos frequente
- Status

### Perguntas
- Qual é o nome do cliente
- Qual é o telefone do cliente
- Qual é o email do cliente
- Qual é o problema do pc
- Quais são as peças trocadas 
- Qual é o valor das peças
- Qual é o valor do serviço
- Qual é o valor total
- Qual é a média de valor gasto
- Qual é o maior valor gasto
- Qual é o menor valor gasto
- Qual é o problema mais frequente
- Qual é o problema menos frequente
- Qual é o status do PC

### Funções
- todos() — abre o CSV e retorna todas as linhas como lista.
- por_nome() — filtra clientes pelo nome exato.
- por_problema() — filtra clientes pelo tipo de problema.
- por_peca() — filtra clientes pela peça trocada.
- pendentes() — retorna só os clientes com status "Pendente".
- resolvidos() — retorna só os clientes com status "Resolvido".
- contar_pendentes() — conta quantos clientes estão pendentes.
- contar_resolvidos() — conta quantos clientes foram resolvidos.
- problema_mais_frequente() — retorna o problema que mais aparece no CSV.
- problema_menos_frequente() — retorna o problema que menos aparece.
- maior_valor_gasto() — retorna o nome do cliente e o maior orçamento.
- menor_valor_gasto() — retorna o nome do cliente e o menor orçamento.
- media_de_valor() — calcula a média de todos os orçamentos.
- contar() — conta o total de clientes.