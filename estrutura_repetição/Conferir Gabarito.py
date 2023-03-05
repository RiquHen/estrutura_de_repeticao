"""Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões,
o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar
com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa).
Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai
utilizar o sistema. Após todos os alunos terem respondido informar:
a. Maior e Menor Acerto;        b. Total de Alunos que utilizaram o sistema;
c. A Média das Notas da Turma.
Gabarito da Prova: 01 - A  02 - B  03 - C  04 - D  05 - E  06 - E  07 - D  08 - C  09 - B  10 - A
Após concluir isto você poderia incrementar o programa permitindo que o professor digite o
gabarito da prova antes dos alunos usarem o programa."""

print("GABARITO: 01 - A  02 - B  03 - C  04 - D  05 - E  06 - E  07 - D  08 - C  09 - B  10 - A")
gaba = ["A", "B", "C", "D", "E", "E", "D", "C", "B", "A"]
nota = questoes = 0
alunos = []
certas = []
continuar = str(input("Conferir o gabarito? [N] - sair: ")).strip().upper()
while continuar != "N":
    nome = input("Nome do Aluno: ")
    alunos.append(nome)
    for i in range(1, len(gaba)+1):
        resposta = str(input(f"Resposta da questão {i}: ")).strip().upper()
        if resposta == gaba[i-1]:
            nota += 1
        certas.append(nota)
        questoes += 1
    print(f"Número de acertos: {nota} questões")
    nota = 0
    continuar = input("Conferir o gabarito novamente? [N] - sair: ")
    if continuar == "N":
        break
    