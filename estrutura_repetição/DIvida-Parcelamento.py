"""Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
a. Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67"""

parcela = float(input("Informe o valor da parcela: "))
print(70*"=")
print(f"{'Divida':^10} {'Valor Juros':>17}{'Nº de Parcelas':^24} {'Valor da Parcela':>9}")
print(70*"-")
for i in range(1, 13):
    juros = 0
    if i % 3 == 0 or i == 1:
        n_parc = i
        val_parc = (parcela + juros) / n_parc
        if i == 3:
            juros = parcela * 10 / 100
            n_parc = i
            val_parc = (parcela + juros) / n_parc
        elif i == 6:
            juros = parcela * 15 / 100
            n_parc = i
            val_parc = (parcela + juros) / n_parc
        elif i == 9:
            juros = parcela * 20 / 100
            n_parc = i
            val_parc = (parcela + juros) / n_parc
        elif i == 12:
            juros = parcela * 25 / 100
            n_parc = i
            val_parc = (parcela + juros) / n_parc
        print(f"R$ {parcela:.2f} {'R$':>6} {juros:^12,.2f} {n_parc:>9} {'R$':>14} {val_parc:.2f}")
print(70*"-")