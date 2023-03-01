"""A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
 Faça um programa capaz de gerar a série até o n−ésimo termo."""

inicio = 0
fim = 1
auxiliar = 0
ultimo_valor = int(input('Informe o ultimo valor da sequência: '))
for i in range(30):
    print(fim, end=' ')
    auxiliar = fim
    fim += inicio
    inicio = auxiliar
    if fim >= ultimo_valor:
        print(f"\nSequência ja atingiu um valor maior que {ultimo_valor}. VALOR: {fim}")
        break
