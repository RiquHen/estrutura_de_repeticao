"""Faça um programa que calcule o número médio de alunos por turma. Para isto,
peça a quantidade de turmas e a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos."""

turmas = int(input("Informe o número de turmas: "))
soma_alunos = 0
for i in range(turmas):
    alunos = int(input(f"Alunos na turma{i+1}: "))
    while alunos >40:
        print("Número inválido. As turmas não podem ter mais de 40 alunos!")
        alunos = int(input(f"Alunos na turma{i + 1}: "))
    soma_alunos += alunos
    media = soma_alunos / turmas
print(f"A média de alunos por turma é: {media:.1f} alunos.")