# 🍔 Food-truck Sabor Express

Sistema de pedidos para food truck feito em Python, rodando no terminal. Permite montar o pedido, ver o carrinho e gerar o recibo com desconto.

## ✨ Funcionalidades

- Menu interativo no terminal (com tabelas usando a biblioteca `rich`)
- Cardápio com lanches, porções e bebidas em tamanhos P, M e G
- Montagem de pedido com quantidade de cada item
- Visualização do carrinho com subtotal e total
- Desconto automático:
  - Com cartão fidelidade: **5%** (pedidos abaixo de R$ 100) ou **20%** (a partir de R$ 100)
  - Sem cartão fidelidade: **10%** (a partir de R$ 100)
- Recibo final com código do pedido

## 🛠️ Tecnologias

- Python 3.10+ (usa `match/case`)
- [rich](https://github.com/Textualize/rich)

## ▶️ Como executar

1. Clone o repositório:

```bash
git clone https://github.com/samykuroda/sistema-pedidos-sabor-express.git
cd sistema-pedidos-sabor-express
```

2. Instale a dependência:

```bash
pip install rich
```

3. Rode o programa:

```bash
python sabor_express.py
```

> O programa usa `cls` para limpar a tela, então foi pensado para rodar no **Windows**.

## 📋 Cardápio

| Item | P | M | G |
|---|---|---|---|
| Clássico Burguer | R$ 18 | R$ 24 | R$ 30 |
| Duplo Bacon | R$ 24 | R$ 30 | R$ 38 |
| Veggie Truck | R$ 20 | R$ 26 | R$ 32 |
| Hot Dog Especial | R$ 14 | R$ 18 | R$ 22 |
| Batata Rústica | R$ 12 | R$ 16 | R$ 20 |
| Limonada | R$ 8 | R$ 10 | R$ 12 |
| Refrigerante | R$ 6 | R$ 8 | - |

## 📚 Aprendizados

Projeto feito para praticar listas, dicionários, funções, laços de repetição, tratamento de erros (`try/except`) e `match/case`.

## 👩‍💻 Autora

Feito por Samira Kuroda · [GitHub](https://github.com/samykuroda)
