"""Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto,
o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um prograltura_mais_alto que
pergunte a cada um dos clientes da academia seu código, sua altura e seu peso.
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
Ao encerrar o prograltura_mais_alto taltura_mais_baixoém deve ser informados os códigos e valores do cliente mais alto,
do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes"""

codigo_mais_alto = codigo_mais_baixo = codigo_mais_gordo = codigo_mais_magro = 0
# codigo_mais_alto = cod+alto - codigo_mais_baixo = cod+baixo - codigo_mais_gordo = cod +gordo - codigo_mais_magro = cod +magro
altura_mais_alto = 0  # altura do mais alto
altura_mais_baixo = 3  # altura do mais baixo
peso_mais_gordo = 0  # peso do mais gordo
peso_mais_magro = 1000  # peso do mais magro
# codigo_mais_alto = cod+alto - codigo_mais_baixo = cod+baixo - codigo_mais_gordo = cod +gordo - codigo_mais_magro = cod +magro
cod = int(input("Informe o código do cliente: "))
while cod != 0:
    alt = float(input("Informe sua altura: "))
    peso = int(input("Informe seu peso: "))
    a = alt
    if alt > altura_mais_alto:
        codigo_mais_alto = cod
        altura_mais_alto = alt
    elif alt <= altura_mais_baixo:
        codigo_mais_baixo = cod
        altura_mais_baixo = alt
    if peso > peso_mais_gordo:
        codigo_mais_gordo = cod
        peso_mais_gordo = peso
    elif peso < peso_mais_magro:
        codigo_mais_magro = cod
        peso_mais_magro = peso
    cod = int(input("Informe o código do cliente[0-Sair]: "))
print(40 * "=")
print(
    f"O código do cliente mais alto: {codigo_mais_alto} ele tem {altura_mais_alto:.2f} metros de altura.")
print(
    f"O código do cliente mais baixo: {codigo_mais_baixo} ele yem {altura_mais_baixo:.2f} metros de altura.")
print(
    f"O código do cliente mais pesado: {codigo_mais_gordo} ele pesa {peso_mais_gordo} kG.")
print(
    f"O código do cliente mais magro: {codigo_mais_magro} ele pesa {peso_mais_magro} kG.")
