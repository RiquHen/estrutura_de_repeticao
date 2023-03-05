"""Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato."""

num_eleitor = int(input("Informe o número de eleitores: "))
cand_a = cand_b = cand_c = 0
print(30*"=", "\n[1] Candidato A\n[2] Candidato B\n[3] Candidato C\n", 30*'=')
for i in range(num_eleitor):
    voto = int(input("Insira o número do seu candidato de preferência: "))
    while voto != 1 and voto !=2 and voto !=3:
        print("Número do candidato inválido!")
        print(30 * "=", "\n[1] Candidato A\n[2] Candidato B\n[3] Candidato C\n", 30 * '=')
        voto = int(input("Insira o número do seu candidato de preferência: "))
    if voto == 1:
        cand_a += 1
    elif voto == 2:
        cand_b += 1
    elif voto == 3:
        cand_c += 1
print(f"{30*'*'}\nTotal de votos: {num_eleitor}\nO candidato A obteve  o total de {cand_a} votos.")
print(f"O candidato B obteve  o total de {cand_b} votos")
print(f"O candidato C obteve  o total de {cand_c} votos")

