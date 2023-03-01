"""Faça um programa que calcule o fatorial de um número inteiro
fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120"""
fat = 1
num = int(input("Informe um número para saber seu fatorial: "))
""" ABAIXO CALCULO DO FATORIAL DE NUMEROS MENORES QUE 16
while 0 > num or num > 16:
    print("Numero inválido. Por favor apenas número entre 1 e 16.")
    num = int(input("Informe um número para saber seu fatorial: "))
"""
print(f"Fatorial de: {num}")
while 0 < num:
    print(num, end=" ")
    if num != 1:
        print("*", end=" ")
    fat *= num
    num -= 1
if 0 < num or num <= 16:
    print(" = ", fat)
