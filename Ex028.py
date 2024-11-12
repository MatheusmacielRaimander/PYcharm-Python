from random import randint
from time import sleep
computador = randint(0,5) #faz o computador "PENSAR"
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Pensei no número: '))
print('Processando...')
sleep(1)
if jogador == computador:
    print('PARABENS!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(computador, jogador))