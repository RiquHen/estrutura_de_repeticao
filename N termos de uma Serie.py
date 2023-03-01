"""Faça um programa que mostre os n termos da Série a seguir:
a.   S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
Imprima no final a soma da série."""

num = int(input("Numero de termos: "))
n = []
m = []
nn = nm = 1
soma = 0
for i in range(num):
    soma += nn / nm
    n.append(nn)
    m.append(nm)
    nn += 1
    nm += 2

for i in range(len(n)):
    if i == len(n)-1:
        print(f" {n[i]}/{m[i]} ",end="")
    else:
        print(f" {n[i]}/{m[i]} ", end="+")
print(f"Soma = {soma:.2f}")
