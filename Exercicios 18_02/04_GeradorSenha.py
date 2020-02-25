#
# @felipecandian
#

from random import choice


print("Gerador de senha ")

quantidade = int(input("Digite a quantidade de caracteres que deseja ter na senha: "))

def gerador_senha(tamanho):
    caracteres = "0123456789abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@!#$%&*()_+}{`^?;:>/-+.,"
    senha = ""

    if quantidade >= 6:   
      for i in range(tamanho):
          senha += choice(caracteres)
      return senha
         
    elif quantidade < 6:
      print("O tamanho da senha tem que ser maior que 6")

senha = gerador_senha(quantidade)      
print("Sua senha gerada é: {}".format(senha))
    


