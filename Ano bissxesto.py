from time import sleep
from datetime import date

print('=-=' * 20)
print('Ano bissexto')
print('=-=' * 20)

ano = int(365)
print('Escreva 0 para ano atual.')
resposta = int(input('Diga um ano e vou verificar se é bissexto: '))
anoB = resposta % 4
anobc = resposta % 400
anobca = resposta % 100
anoatual = date.today().year
if resposta == 0:
    if  anoatual % 4 == 0 and anoatual % 100 ==0:
        print('{} É um ano bissexto.'.format(anoatual))

    else:
        print('{} Nao é um ano bissexto.'.format(anoatual))
else:
    if anoB == 0 and anobca != 0:
        print('{} É um ano bissexto.'.format(resposta))

    elif anobc == 0:
        print('{} É um ano bissexto.'.format(resposta))

    else:
        print('{} Nao é um ano bissexto.'.format(resposta))


