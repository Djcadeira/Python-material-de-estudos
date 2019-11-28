import time


num = int(input('\033[30mDigite um numero: '))
numinicial = num
vezes = int(1)
historico = list

#4 digitos em int separados por variaveis
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

#lista convertida em decrecente 4321
lista = [u, d, c, m]
lista = sorted(lista, key=int, reverse=True)
dc1 = lista[0] * 1000
dc2 = lista[1] * 100
dc3 = lista[2] * 10
dc4 = lista[3] * 1
dc5 = dc1 + dc2 + dc3 + dc4

#lista convertida em crescente 1234
lista = [u, d, c, m]
lista = sorted(lista, key=int)
cr1 = lista [0] * 1000
cr2 = lista [1] * 100
cr3 = lista [2] * 10
cr4 = lista [3] * 1
cr5 = cr1 + cr2 + cr3 + cr4
conta = dc5 - cr5
historico = conta
print('{} - {} = {}'.format(dc5, cr5, conta))
print(historico,vezes)


while (conta != int(6174)):
    num = conta
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10

    lista = [u, d, c, m]
    lista = sorted(lista, key=int, reverse=True)
    dc1 = lista[0] * 1000
    dc2 = lista[1] * 100
    dc3 = lista[2] * 10
    dc4 = lista[3] * 1
    dc5 = dc1 + dc2 + dc3 + dc4

    lista = sorted(lista, key=int)
    cr1 = lista[0] * 1000
    cr2 = lista[1] * 100
    cr3 = lista[2] * 10
    cr4 = lista[3] * 1
    cr5 = cr1 + cr2 + cr3 + cr4
    conta = dc5 - cr5
    print('{} - {} = {}'.format(dc5, cr5, conta))
    historico = conta
    vezes = vezes + 1
    print(historico, vezes)
    time.sleep(3)
else:
    print('Com apenas {} vezes {} virou 6174.'.format(vezes,numinicial))