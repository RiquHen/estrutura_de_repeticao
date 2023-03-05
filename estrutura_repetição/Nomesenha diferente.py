"""Faça um programa que leia um nome de usuário
 e a sua senha e não aceite a senha igual ao nome do usuário,
 mostrando uma mensagem de erro e voltando a pedir as informações."""
import getpass

nome = input("Nome de usuário: ")
# getpass oculta sua digitação para não exibir a senha digitada
senha = getpass.getpass("Senha: ")
while nome == senha:
    print("Erro. Senha nao pode ser o nome de usuário!")
    nome = input("Nome de usuário: ")
    senha = input("Senha: ")

print(f"{'-'*30}\nUsuário: {nome}\nSenha: {senha}\n{'-'*30}")
print(f"Login realizado com sucesso!\nBem vindo, sr. {nome}!\n{'='*30}")