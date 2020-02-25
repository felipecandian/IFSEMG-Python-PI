#
# @felipecandian
#

from random import randint
r = 'S'
while r == 'S':
  itens = ('Pedra', 'Papel', 'Tesoura') #Array com as jogadas
  computador = randint(0,2) #Criação de números randomicos

  #Menu de opções
  print("JOKENPO!\nEscolha: \n[ 0 ] - Pedra \n[ 1 ] - Papel \n[ 2 ] - Tesoura")
  jogador = int(input('Qual é a sua jogada? \n::'))

  print('===================================')
  print('PlayerComputador jogou {}'.format(itens[computador]))
  print('Player jogou {}'.format(itens[jogador]))
  print('===================================')

  if computador == 0:
    if jogador == 0:
      print("Você empatou")
    elif jogador == 1:
      print("Você venceu")
    elif jogador == 2:
      print("Você perdeu")
    else:
      print("JOGADA INVALIDA")

  elif computador == 1:
    if jogador == 0:
      print("Você perdeu")
    elif jogador == 1:
      print("Você empatou")
    elif jogador == 2:
      print("Você venceu")
    else:
      print("JOGADA INVALIDA")

  elif computador == 2:
    if jogador == 0:
      print("Você venceu")
    elif jogador == 1:
      print("Você perdeu")
    elif jogador == 2:
      print("Você empatou")
    else:
      print("JOGADA INVALIDA")
  r = str(input('Quer continuar? [S/N]')).upper()