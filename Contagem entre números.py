"""Faça um programa que receba dois números inteiros e
gere os números inteiros que estão no intervalo compreendido por eles."""
soma = 0
num1 = int(input("Informe o início da contagem: "))
num2 = int(input("Informe o final da contagem: "))
for i in range(num1,num2+1):
    print(i, end=' ')
    soma += i
print(f"\nA soma dos númeno no intervalo {num1} a {num2} é: {soma}")