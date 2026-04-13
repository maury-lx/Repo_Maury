import random
facce = int(input("Inserisci il numero di facce dei dadi: "))



dado1 = random.randint(1, facce)
print("Il numero uscito sul primo dado è:", dado1)
dado2 = random.randint(1, facce) 
print("Il numero uscito sul secondo dado è:", dado2)
if dado1 == dado2:
    print("Hai vinto")
else:
    print("Non hai vinto")
