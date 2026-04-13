miaeta = int(input("Inserisci la tua età: "))
documentovalido = bool(input("Il tuo documento è valido? (Si/No): "))

if miaeta >= 18 and documentovalido:
    print("Si puoi accedere al club")
elif miaeta < 18 and documentovalido:
    print("Mi dispiace non puoi accedere al club")
elif miaeta > 18 and not documentovalido:
    print("Mi dispiace non puoi accedere al club")
elif miaeta < 18 and not documentovalido:
    print("Mi dispiace non puoi accedere al club")
