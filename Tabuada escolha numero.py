"""Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer
 número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver
  a tabuada. """

num = int(input("Informe um número[entre 1 e 10] para ver sua tabuada: "))
while num < 0 or num > 10:
    print("Numero inválido! Apenas número entre 1 e 10.")
    num = int(input("Informe um número[entre 1 e 10] para ver sua tabuada:  "))
for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')