"""Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
a. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
b. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
c. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro
do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário.
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário."""

import datetime
aumento: float = 1.5 / 100
conta_ano = 0
# salario = 1000
# ano_inicial = 1995
ano_atual = datetime.datetime.now().year
ano_inicial = int((input("Informe o ano de inicio do trabalho: ")))
print(50*'=')
while ano_inicial > ano_atual:
    print(f"O ano informado {ano_inicial} é maior que o ano atual. {ano_atual}\n{50*'='}"
          f"\n{'Por favor, corrija!':^40}\n{50*'-'}")
    ano_inicial = int((input("Informe o ano de inicio do trabalho: ")))
salario = float(input("Informe o salario inicial: "))
for i in range(ano_inicial+1,ano_atual+1):
    conta_ano += 1
    v_aum = salario * aumento
    salario = salario + v_aum
    print(f"Em {i} com o aumento de {aumento*100:.1f}% = R$ {v_aum:.2f} o salario passou a ser: R$ {salario:.2f}")
    if conta_ano % 3 == 0:
        aumento += aumento
        conta_ano = 0


