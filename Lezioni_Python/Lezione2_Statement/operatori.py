# OPERATORI DI CONFRONTO (producono un boolean)
# == uguale a  (1 ==1)

confronto1 = (10 > 5)
print(confronto1)

conf3 = 10 == 9
print(conf3)

parola = "Ciao"
saluto = "ciao"
conf4 = (parola == saluto)
print(conf4)

conf5 = (parola.lower() == saluto.lower())
print(conf5)

conf6 = (len(parola) == len(saluto))
print(conf6)

miaEta = int(input("Quanti anni hai?"))
if miaEta >= 18:
    print("Sei maggiorenne")
elif miaEta > 18:
    print("Sei minorenne")
else:
    print("Valore non valido")

oradelgiorno = 16

if oradelgiorno > 0 and oradelgiorno <= 9:
    print("Buon mattino")
elif oradelgiorno > 9 and oradelgiorno < 19:
    print("Buon pomeriggio")
    