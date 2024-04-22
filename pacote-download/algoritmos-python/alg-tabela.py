idade = int(input("Digite a idade do atleta"))
if idade < 5:
    print("Não tem idade para ser atleta")
elif idade <= 7:
    print("Infantil A")
elif idade <= 10:
    print("Infatil B")
elif idade <= 13:
    print("Juvenil A")
elif idade <= 17:
    print("Juvenil B")
else:
    print("Sênior")