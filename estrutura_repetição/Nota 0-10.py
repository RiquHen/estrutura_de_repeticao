"""Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até
que o usuário informe um valor válido."""

nota = int(input("Informe o valor da nota(0 a 10): "))
while nota < 0 or nota > 10:
    print("Valor de nota digitado errado!!! Tente novamente.")
    nota = int(input("Informe o valor da nota(0 a 10): "))
print(f'Sua nota foi: {nota}')