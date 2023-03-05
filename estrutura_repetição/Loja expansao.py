""" O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99
e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa
registradora rudimentar. O programa deverá receber um número desconhecido de valores
referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador
para indicar o final da compra. O programa deve então mostrar o total da compra e
perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor
do troco. Após esta operação, o programa deverá voltar ao ponto inicial,
para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
        a. Lojas Tabajara
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00"""
produtos = []
precos = []
quant = []
soma = 0
produto = input("Produto: ")
while produto != "0":
    produtos.append(produto)
    preco = float(input("Informe o preço: "))
    precos.append(preco)
    quants = int(input("Informe a quantidade: "))
    quant.append(quants)
    valor = quants * preco
    soma += valor
    produto = input("Produto: ")
print(40*"=")
dinheiro = float(input("valor recebido: "))
print(40*"=")
print(f"{'Produtos':>20}{'Preços':^12}Quantidade\n{50*'-'}")
for i in range(len(precos)):
    print(f"Produto {i+1}: {produtos[i]:^10}| R$ {precos[i]:.2f}| {quant[i]:^8}")
print(47 * "-")
print(f"Total a pagar: {'R$':>14} {soma:.2f}")
print(f"Valor recebido: {'R$':>13} {dinheiro:.2f}")
print(47*"-")
print(f"Troco: {'R$':>22} {dinheiro - soma:.2f}")