"""Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50."""
n = int(input("insira final da contagem: "))
for i in range(n):
    if i % 2 == 1:
        print(i, end=" ")