"""Faça um programa que leia 5 números e informe o maior número."""
maior = soma = 0
for i in range (5):
    # entrada de 5 numeros
    num = int (input("Digite um numero: "))
    if num > maior:
        maior = num
    soma += num
print(f"O maior número digitado foi o {maior}.")
print(f"A soma dos números digitados é: {soma}")
print(f"A média dos números digitados é: {soma/5:.2f}")