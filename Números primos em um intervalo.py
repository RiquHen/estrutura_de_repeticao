"""Faça um programa que mostre todos os primos entre 1 e N
sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar
os números primos. Serão avaliados o funcionamento, o estilo e o número de testes
(divisões) executados."""

num = int(input("Informe um nuúmero inteiro: "))
contador = conta_primo = 0
for i in range(1, num+1):
    for j in range(1, i+1):
        if i % j == 0:
            contador += 1   # conta o número de divisores
    if contador > 2:
        conta_primo += 1 # conta as divisões realizadas
        print(f"{i} não é primo! Foram feitas  {conta_primo} divisões. Contador: {contador}")
        contador = 0
        """print("O número é divisível por:", end=" ")
        for i in range(1, num + 1):
            if num % i == 0:
                print(i,end=" ")"""
    else:
        conta_primo += 1
        print(f"{i} é primo! Foram feitas {conta_primo} divisoes. Contador: {contador}")
        contador = 0
