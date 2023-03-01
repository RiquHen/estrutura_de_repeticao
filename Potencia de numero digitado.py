"""Faça um programa que peça dois números, base e expoente,
calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem."""

base = int(input("Informe a base: "))
expoente = int(input("informe o expoente: "))
total = base
for i in range(1, expoente):
    total *= base
print(f"{base} elevado a {expoente} é igual a {total}")