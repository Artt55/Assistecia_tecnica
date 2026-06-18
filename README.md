# 🖥️ Assistência Técnica — Projeto Integrador 2026
### SENAC Tech

> Sistema de gerenciamento de clientes para uma assistência técnica de computadores, desenvolvido em Python com armazenamento em CSV.

---

## 📋 Dados armazenados

| Campo | Descrição |
|---|---|
| Nome | Nome completo do cliente |
| Telefone | Contato do cliente |
| Email | Email do cliente |
| Problema do PC | Tipo de problema identificado |
| Peças trocadas | Peças utilizadas no reparo |
| Valor das peças | Custo das peças (R$) |
| Valor do serviço | Custo da mão de obra (R$) |
| Valor total | Orçamento final (R$) |
| Status | Pendente ou Resolvido |

---

## 📁 Arquivos

| Arquivo | Descrição |
|---|---|
| `clientes_assistencia.csv` | Base de dados dos clientes |
| `dbassistencia_tecnica.py` | Funções de acesso e filtro dos dados |
| `viewassistencia.py` | Função de exibição dos clientes no terminal |
| `contar_clientes.py` | Exibe todos os clientes e totais por status |
| `listar_por_nome.py` | Busca clientes pelo nome |
| `listar_por_problema.py` | Busca clientes pelo problema do PC |
| `listar_por_peca.py` | Busca clientes pela peça trocada |
| `listar_pendentes.py` | Lista todos os clientes com status Pendente |
| `listar_resolvidos.py` | Lista todos os clientes com status Resolvido |
| `cadastrar_cliente.py` | Cadastra um novo cliente no sistema |
| `relatorio.py` | Exibe estatísticas gerais do sistema |

---

## ⚙️ Funções — `dbassistencia_tecnica.py`

**Acesso aos dados**
- `todos()` — retorna todos os clientes do CSV
- `contar()` — retorna o total de clientes

**Filtros**
- `por_nome(nome)` — filtra clientes pelo nome exato
- `por_problema(problema)` — filtra clientes pelo tipo de problema
- `por_peca(peca)` — filtra clientes pela peça trocada
- `pendentes()` — retorna clientes com status Pendente
- `resolvidos()` — retorna clientes com status Resolvido

**Contagem**
- `contar_pendentes()` — conta clientes pendentes
- `contar_resolvidos()` — conta clientes resolvidos

**Estatísticas gerais**
- `problema_mais_frequente()` — problema mais comum no geral
- `problema_menos_frequente()` — problema menos comum no geral
- `maior_valor_gasto()` — cliente com maior orçamento
- `menor_valor_gasto()` — cliente com menor orçamento
- `media_de_valor()` — média de valor gasto por cliente

**Estatísticas por status**
- `problema_mais_frequente_resolvidos()` — problema mais comum entre resolvidos
- `problema_menos_frequente_resolvidos()` — problema menos comum entre resolvidos
- `problema_mais_frequente_pendentes()` — problema mais comum entre pendentes
- `problema_menos_frequente_pendentes()` — problema menos comum entre pendentes

**Cadastro**
- `cadastrar()` — adiciona um novo cliente ao CSV

---

## ▶️ Como executar

```bash
# Listar todos os clientes
python contar_clientes.py

# Buscar por nome
python listar_por_nome.py

# Ver relatório estatístico
python relatorio.py

# Cadastrar novo cliente
python cadastrar_cliente.py
```
