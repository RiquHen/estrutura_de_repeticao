"""Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1."""

num = int(input("Informe um número para saber se ele é primo: "))
contador = 0
for i in range(1, num+1):
    if num % i == 0:
        contador += 1
if contador > 2:
    print("O número digitado não é primo!")
    print("O número é divisível por:", end=" ")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i,end=" ")
else:
    print("O número digitado é primo!")
