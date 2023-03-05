"""Faça um programa que peça um numero inteiro positivo e em seguida
mostre este numero invertido.
a. Exemplo:     12376489 => 98467321"""

n = 12376489
# Primeiro Método
inv_n = int(str(n)[::-1])
print(inv_n)

# Segundo Método
print(40*"=")
n = int(input("Digite um número para ser invertido: "))
s_n = str(n)
print(f"{40*'-'}\nNúmero Digitado: {n}")
print("Número Invertido: ", end="")
for i in range(len(s_n)-1, -1, -1):
    print(s_n[i],end="")


