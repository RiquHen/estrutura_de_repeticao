"""    2. Faça um programa que leia e valide as seguintes informações:
        a. Nome: maior que 3 caracteres;
        b. Idade: entre 0 e 150;
        c. Salário: maior que zero;
        d. Sexo: 'f' ou 'm';
        e. Estado Civil: 's', 'c', 'v', 'd'"""
nome = str(input("Nome: "))
while len(nome) <= 3:
    print("Nome deve ter mais de 3 caracteres!")
    nome = str(input("Nome: "))
idade = int(input("Idade: "))
while idade < 0 or idade > 150:
    print("Idade inválida!")
    idade = int(input("Idade: "))
salario = float(input("Salário: "))
while salario < 0:
    print("Valor do salário inválido!")
    salario = float(input("Salário: "))
sexo = str(input("Sexo(F ou M): ")).strip().upper()
while sexo != "F" and sexo != "M":
    print("Sexo inválido!")
    sexo = str(input("Sexo(F ou M):")).strip().upper()
print("[S] - Solteiro\n[C] - Casado\n[V] - Viúvo\n[D] - Divorciado")
est_civil = str(input("Estado Civil: ")).strip().upper()
while est_civil not in 'SDCV':
    print("Estado civil inválido!")
    est_civil = str(input("estado Civil: ")).strip().upper()

if est_civil == "S":
    est_civil = "Solteiro"
elif est_civil == "C":
    est_civil = "Casado"
elif est_civil == "V":
    est_civil = "Viúvo"
elif est_civil == "D":
    est_civil = "Divorciado"

if sexo == "F":
    sexo_r = "Feminino"
elif sexo == "M":
    sexo_r = "Masculino"

print(f"{40*'~'}\n{'Cadastro':^40}\n{40*'~'}\nNome: {nome}\nIdade: {idade}\nSalário: R$ {salario:.2f}")
print(f"Sexo: {sexo_r}\nEstado Civil: {est_civil}\n{40*'~'}")