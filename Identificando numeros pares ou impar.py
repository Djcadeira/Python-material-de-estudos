import time

repetiçao = 0
resposta = 0

while True:
    num = int(input('Diga um numero vou retornar se ele é par ou impar: '))
    print('\nPROCESSANDO')
    paridade = num % 2
    time.sleep(2)
    if paridade == 0:
        print('\n{} é par'.format(num))
        time.sleep(2)
        resposta = input('Deseja continuar ? \n')
        resposta = resposta.lower()

        if resposta.find('nao') == 0:
            print('Finalizando.')
            quit()
            

    else:
        print('\n{} é impar'.format(num))
        repetiçao = repetiçao + 1
        resposta = input('Deseja continuar ? \n')
        resposta = resposta.lower()

        if resposta.find('nao') == 0:
            print('Finalizando.')
            quit()
      

    

