import time

velocidadeM = 80
velocidade = int(input('Diga a velocidade do carro: '))
if velocidade > velocidadeM:
    ultrapassado = velocidade - velocidadeM
    multa = ultrapassado * 7
    print('Voce foi multado em {} Reais, por ultrapassar {}Km/H do limite de 80Km/H'.format(multa,ultrapassado))
else:
   print('Esta dentro dos conformes siga assim.')