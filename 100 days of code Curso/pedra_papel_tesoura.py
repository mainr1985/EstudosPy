import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Bem vindo(a) ao Pedra, Papel e Tesoura - Edição Python!")
choice1 = int(
    input(
        "Qual a sua escolha? Pressione 0 para Pedra, 1 para Papel ou 2 para Tesoura: \n"
    ))
if choice1 == 0:
    print("Você escolheu Pedra:")
    print(pedra)
elif choice1 == 1:
    print("Você escolheu Papel:")
    print(papel)
elif choice1 == 2:
    print("Você escolheu Tesoura:")
    print(tesoura)

#escolha do computador
choice2 = random.randint(0, 2)
if choice2 == 0:
    print("O computador escolheu Pedra:")
    print(pedra)
    if choice1 == 1:
        print("Papel cobre Pedra - você ganhou! :D ")
    elif choice1 == 2:
        print("Pedra esmaga Tesoura - você perdeu. :( ")   
    
elif choice2 == 1:
  print("O computador escolheu Papel:")
  print(papel)
  if choice1 == 0:
    print("Papel cobre Pedra - você perdeu! :( ")  
  elif choice1 == 2:
    print("Tesoura corta Papel - você ganhou! :D ")   

elif choice2 == 2:
  print("O computador escolheu Tesoura:")
  print (tesoura)
  if choice1 == 0:
    print("Pedra esmaga Tesoura - você venceu! :D ")
  elif choice1 == 1:
    print("Tesoura corta Papel - você perdeu! :( ")   

if choice1==choice2:
    print("Deu empate. Jogue de novo.")  