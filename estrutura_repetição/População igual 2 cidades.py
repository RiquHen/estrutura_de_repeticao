"""Supondo que a população de um país A seja da ordem de 80000 habitantes
com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes
com uma taxa de crescimento de 1.5%. Faça um programa que calcule e
escreva o número de anos necessários para que a população do país A
ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento."""

populacao_cidade_a = 120000
populacao_cidade_b = 200000
anos = 0

while populacao_cidade_a <= populacao_cidade_b:
    crescimento_cidade_a = 0.03 * populacao_cidade_a
    crescimento_cidade_b = 0.015 * populacao_cidade_b
    populacao_cidade_a = populacao_cidade_a + crescimento_cidade_a
    populacao_cidade_b = populacao_cidade_b + crescimento_cidade_b
    print(
        f"População a: {populacao_cidade_a:.0f} habitantes - População b: {populacao_cidade_b:.0f} habitantes")
    anos += 1

print(
    f"A população da cidade A demorará {anos} anos, para ultrapassar a população da cidade b")
print(f"{40*'*='}")
"""Altere o programa anterior permitindo ao usuário informar as populações 
e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação."""
