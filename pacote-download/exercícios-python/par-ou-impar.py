#Par ou impar com o computador
import random
escolha = input("Par ou impar?")
apostaJ = int(input("Quantos dedos vc vai lançar?"))
apostaC = random.randint(0,10)
print("Computador: ", apostaC)
soma = apostaJ + apostaC
if soma % 2 == 0 and escolha == 'par':
    print("Vc ganhou!!")
elif soma % 2 != 0 and escolha == 'impar':
    print("Vc ganhou!!")
else:
    print("Vc perdeu!")