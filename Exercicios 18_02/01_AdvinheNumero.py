#
# @felipecandian
#

from random import randint

r = 'S'
print('Qual é o seu palpite?')
numero = randint(0,20) #Criação de números randomicos
while r == 'S':
  #Menu de opções
  palpite = int(input('::'))

  if palpite == numero:
    print("Parabens acertou")
    r = str(input('Quer continuar? [S/N]')).upper()

  elif palpite > numero:
    print("Menor")

  elif palpite < numero:
    print("Maior")

  else:
    print("JOGADA INVALIDA")

  print('===================================')


