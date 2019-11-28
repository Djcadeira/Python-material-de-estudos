import time
cor = {'limpa' : '\033[m',
       'pretoebranco' : '\033[7:30m',
       'branco0' : '\033[30m',
       'vermelho1': '\033[31m',
       'verde2' : '\033[32m',
       'azul4' : '\033[34m',
       'magenta5' : '\033[35m',
       'amarelo3' : '\033[33m'
        }

print('Sou um bot de financiamento de casas...')
print('Vamos começar...')

# Condiçao da renda.
salario = int(input('\nInforme sua renda/mes.\n'))
if salario <= 998 and salario >= 800:
    resposta = input('{}R$ é equivalente a um salario minimo, tem certeza que deseja comprar uma casa nesse momento? '.format(salario))
    if resposta.lower().find('sim') != -1:
        print('Muito cuidado com as dividas, informo que nossa politica nao permite financiamentos que ultrapassem 30% do seu salario.')
    else:
        time.sleep(2)
        print('FINALIANDO')
        time.sleep(5)
        quit()
elif salario <= 800:
    print('Sua renda é muito baixa.\nFINALIZANDO')
    quit()

elif salario >= 999 and salario <= 1500:
    print('Muito cuidado com as dividas, informo que nossa politica nao permite financiamentos que ultrapassem 30% do seu salario.')
else:
    print(' ')
#Condiçao de financiamento.
casa = int(input('Quanto custa a casa que deseja comprar? '))
if casa >= 200001:
    print('---' * 20)
    print('DELUXE')
    print('---' * 20)
    print('{}R$ É um investimento muito bom...'.format(casa))
elif casa >= 50000 and casa <= 200000:
    print('---' * 20)
    print('FAMILY')
    print('---' * 20)
    print('{}R$ É um excelente investimento...'.format(casa))
elif casa <= 50000 and casa >= 10000:
    print('---' * 20)
    print('HUMILDE PACK')
    print('---' * 20)
    print('{}R$ é o preço de uma casa intermediaria.'.format(casa))
else:
    print('Financiamos apenas valores acima de 10000R$.')
    time.sleep(2)
    print('FINALIZANDO')
    quit()

resposta = input('Deseja pagar a vista ou parcelado? ').lower()
# Problema---------------------------------------------------------
if resposta.find('parcelado') == 0 or resposta.find('parcelas') == 0 or resposta.find('prestaçoes') == 0:
    parcelas = int(input('Em quantas parcelas deseja pagar? '))
    historico = parcelas
    parcelas = salario / parcelas
    limite = (salario * 35) / 100
    tentativa = 0
    anos = historico // 12
    meses = historico % 12
    condiçao2 = casa / historico
# Problema---------------------------------------------------------
    if parcelas > limite:
        while tentativa == 0:
            print('{} parcelas de {}.'.format(historico,parcelas))
            print('Nossa politica nao permite que as parcelas seja 35% maior que a renda.')
            resposta = str(input('Quer tentar aumentar as parcelas ? '))
            print('Seu limite é {}R$\n'.format(limite))
            if resposta.lower().find('sim') != -1 or resposta.lower().find('quero') != -1:
                parcelas = int(input('LEMBRANDO TEM QUE SER MAIOR QUE {}\nnumero de parcelas: '.format(historico)))
                historico = parcelas
                parcelas = salario / parcelas
                limite = (salario * 30) / 100
                condiçao2 = casa / historico
                if parcelas < limite and parcelas >= condiçao2:
                    tentativa = tentativa + 1

            else:
                tentativa = tentativa + 1
    elif parcelas < condiçao2:
        while tentativa == 0:
            print(f'{historico} parcelas nao alcançaram o valor da casa de R${condiçao2}.')
            print('Nossa politica nao permite que as parcelas seja 35% maior que a renda.')
            resposta = str(input('Quer tentar aumentar as parcelas ? '))
            print('Seu limite por parcela é R$ {}\n'.format(limite))
            if resposta.lower().find('sim') != -1 or resposta.lower().find('quero') != -1:
                parcelas = int(input('LEMBRANDO TEM QUE SER MAIOR QUE {}\nnumero de parcelas: '.format(historico)))
                historico = parcelas
                parcelas = salario / parcelas
                limite = (salario * 30) / 100

            else:
                tentativa = tentativa + 1
    else:
        print()
else:
    print('Boa compra.')
    
print('Acordo fechado.')
print('Seu limite é {}'.format(limite))
print('Fechamos em {} parcelas de R$ {}'.format(historico,condiçao2))
print('Aproximadamente {} anos e {} meses.'.format(anos,meses))
