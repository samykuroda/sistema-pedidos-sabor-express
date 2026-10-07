# ======== 𖦹˚｡ PROJETO FOOD-TRUCK SABOR EXPRESS ᡣ🍔୨ৎ========

#Módulos
from rich import print
from rich.console import Console
from rich.table import Table

import os
import emoji
os.system('cls')
#lista com os lanches cadastrados no sistema
cardapio = [
    {"lanche":"clássico burguer", "tamanho":"P", "preco":18},
    {"lanche":"clássico burguer", "tamanho":"M", "preco":24},
    {"lanche":"clássico burguer", "tamanho":"G", "preco":30},
    {"lanche":"duplo bacon","tamanho":"P","preco":24},
    {"lanche":"duplo bacon","tamanho":"M","preco":30},
    {"lanche":"duplo bacon","tamanho":"G","preco":38},
    {"lanche":"veggie truck","tamanho":"P","preco":20},
    {"lanche":"veggie truck","tamanho":"M","preco":26},
    {"lanche":"veggie truck","tamanho":"G","preco":32},
    {"lanche":"hot dog especial","tamanho":"P","preco":14},
    {"lanche":"hot dog especial","tamanho":"M","preco":18},
    {"lanche":"hot dog especial","tamanho":"G","preco":22},
    {"lanche":"batata rustica","tamanho":"P","preco":12},
    {"lanche":"batata rustica","tamanho":"M","preco":16},
    {"lanche":"batata rustica","tamanho":"G","preco":20},
    {"lanche":"limonada","tamanho":"P","preco":8},
    {"lanche":"limonada","tamanho":"M","preco":10},
    {"lanche":"limonada","tamanho":"G","preco":12},
    {"lanche":"refrigerante","tamanho":"P","preco":6},
    {"lanche":"refrigerante","tamanho":"M","preco":8},  
]

pedido_cliente = []

#function calcular subtotal

def calcular_subtotal(preco_item, quant_item):
    subtotal = preco_item * quant_item
    return subtotal

def calcular_total(lista_pedidos):
    total = 0
    for ped in lista_pedidos:
        total += ped["subtotal"]
    return total
    
#Menu principal
while True:
    console = Console()
    tabela = Table(title = "Food-truck Sabor Express")
    tabela.add_column("MENU PRINCIPAL")
    tabela.add_row("1. Montar pedido")
    tabela.add_row("2. Ver carrinho e total ")
    tabela.add_row("3. Finalizar pedido")
    tabela.add_row("4. Sair")
    console.print(tabela)
    opcao = int(input("Digite a opção desejada: "))
    
    match opcao:
        case 1:
            coleta_pedido_cliente = int(input("Digite quantos itens serão adicionados no pedido: "))
            for item in range(1,coleta_pedido_cliente+1):
                nome_item = input(f"Nome do {item}º lanche/bebida: ").lower().strip()
                tamanho_item = input("Tamanho do lanche (P,M ou G): ").upper()
                quant_item = int(input(f"Digite a quantidade desejada de {nome_item}: "))
                
                for i in range(len(cardapio)):
                    if cardapio[i]["lanche"] == nome_item and cardapio[i]["tamanho"] == tamanho_item:
                        preco_item = cardapio[i]["preco"]
                
                subtotal = calcular_subtotal(preco_item, quant_item)
                
                pedido = {
                    "lanche":nome_item,
                    "tamanho":tamanho_item,
                    "quantidade":quant_item,
                    "preco_item":preco_item,
                    "subtotal": subtotal
                }
                
                pedido_cliente.append(pedido)
                
            print("Pedido registrado !!")
                
            input("Digite ENTER para voltar ao menu e finalizar o pedido!")
        case 2:
            if pedido_cliente == []:
                print("Ainda não há itens no carrinho")
                input("Digite ENTER para voltar ao menu e fazer seu pedido...")
            for ped in pedido_cliente:
                print(f"""
    Item: {ped['lanche']}, {ped['tamanho']} ({ped['quantidade']})
    preço: R$ {ped['preco_item']}
    subtotal: R$ {ped['subtotal']}""")
            print(f"total do pedido: R$ {calcular_total(pedido_cliente)}")
            input("Digite ENTER para voltar ao menu e finalizar o pedido!")
        case 3:
            nome_cliente = input("Informe seu nome: ").capitalize().strip()
            codigo = nome_cliente[0:3].upper() + quant_item
            fid_cliente = input("Você possui cartão fidelidade? (s/n) :").lower()
                
            
            
            
            
    
    