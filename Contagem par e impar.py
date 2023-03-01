"""Faça um programa que peça 10 números inteiros,
 calcule e mostre a quantidade de números pares e a quantidade de números impares."""
conta_par = conta_impar = 0
for i in range(10):
    num = int(input("Informe um número: "))
    if num % 2 == 1:
        conta_impar +=1
    else:
        conta_par += 1
print(f"Números pares: {conta_par}\nNúmeros ímpares: {conta_impar}")