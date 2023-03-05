"""Em uma eleição presidencial existem quatro candidatos.
Os votos são informados por meio de código. Os códigos utilizados são:
a. 1 , 2, 3, 4  - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc) 5 - Voto Nulo 6 - Voto em Branco
Faça um programa que calcule e mostre:b. O total de votos para cada candidato;
c. O total de votos nulos;  d. O total de votos em branco;
e. A percentagem de votos nulos sobre o total de votos;
f. A percentagem de votos em branco sobre o total de votos.
Para finalizar o conjunto de votos tem-se o valor zero."""

print(f"{50*'='}\n{'Eleições Fantárdigas:':^50}\n{50*'-'}")
print(f"[1] Zé da Burra{'[4] Voto Nulo':>25}\n[2] Chico da Télvina{'[5] Voto em Branco':>25}"
      f"\n[3] Finado Tabaquinha\n{50*'-'}")


v_nulos = v_branco = 0
cand1 = cand2 = cand3 = voto = soma = 0
while True:
    voto = input("Digite o número do candidato[0 -SAIR): ")
    if voto.isalpha():
        print("Opção Inválida!!!")
    else:
        v = int(voto)
        if v == 0:
            break
        elif 0 < v > 5:
            print("Opção Inválida!!!")
        elif 1 <= v <= 5:
            soma += 1
            if v == 1:
                cand1 += 1
                c1 = "Zé da Burra"
            elif v == 2:
                cand2 += 1
                c2 = "Chico da Télvina"
            elif v == 3:
                cand3 += 1
                c3 = "Finado Tabaquinha"
            elif v == 4:
                v_nulos += 1
            elif v == 5:
                v_branco += 1
print(50*"=")
print(f"Total de votos computados: {soma} votos válidos.")
print(f"O candidato {c1} teve {cand1} votos. Com percentual de {cand1*100/soma:.2f}%")
print(f"O candidato {c2} teve {cand2} votos. Com percentual de {cand2*100/soma:.2f}%")
print(f"O candidato {c3} teve {cand3} votos. Com percentual de {cand3*100/soma:.2f}%")
print(f"{v_nulos} votos nulos. Com porcentagem de {v_nulos*100/soma:.2f}%")
print(f"{v_branco} votos em branco. Com porcentagem de {v_branco*100/soma:.2f}%")

