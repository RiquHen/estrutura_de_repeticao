"""O cardápio de uma lanchonete é o seguinte:
 Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
Considere que o cliente deve informar quando o pedido deve ser encerrado."""
prod = ["Cachorro Quente", "Bauru Simples", "Bauru com ovo", "Hambúrguer","Chesseburguer",
        "Refrigerante"]
cod = [100, 101, 102, 103, 104, 105]
preco = [1.2, 1.3, 1.5, 1.2, 1.3, 1]
print(f"{50*'='}\n{'Cardápio da KiLanche':^50}\n{50*'='}")
print(f"{'Código':^10}|{'Produto':^20}|{'Preço':^17}\n{50*'-'}")
for i in range (5):
    print(f"{cod[i]:^9} |{prod[i]:^20}|{preco[i]:^15,.2f}")
print(f"{50*'-'}\n{'Iniciando Pedido do Cliente':^40}\n{27*'-':^40}")
# *************************************************************************
p = []
quantia = []
soma = []
total = 0
ped = int(input("Informe o código do produto: "))
while ped != 0:
    for i in range(len(cod)):
        if ped == cod[i]:
            p.append(i)
            quantos = int(input("Quantas unidades: "))
            quantia.append(quantos)
            soma.append(quantos*preco[i])
    ped = int(input("Informe o código do produto: "))
print(f"{60*'-'}\n{'Número':^6} {'Código':^8}{'Produto':^18}{'ValorUni'}{'Quantia':^12}{'Valor':>5}")
print(60*'-')
for i in range(len(p)):
    print(f"{i+1:^6}{cod[p[i]]:^10}{prod[p[i]]:^18}{preco[p[i]]:>5,.2f}{quantia[i]:>8}{soma[i]:>10,.2f}")
    total += soma[i]
print(f"{20*'-':>59}\n{'Total a pagar:':>54} {total:.2f}")