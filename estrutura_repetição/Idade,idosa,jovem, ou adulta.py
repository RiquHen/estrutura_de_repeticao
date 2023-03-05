"""Faça um programa que peça para n pessoas a sua idade,
 ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60
 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada."""

pessoas = int(input("Informe o numero de pessoas na turma: "))
soma = 0
for i in range(pessoas):
    idade = int(input(f"Informe a idade da {i+1}ª pessoa: "))
    soma += idade
media = soma / pessoas
if 0 < media <= 25:
    print(f"Essa turma é jovemm com media de idade de {media:.0f} anos.")
elif 25 < media < 60:
    print(f"Essa turma é adulta, com média de idade de {media:.0f} anos.")
elif media > 60:
    print(f"Essa turma é idosa, com a média de idade de {media:.0f} anos.")