user = (input("Qualè il tuo nome utente?"))
password = (input("Qualè la tua password?"))    

if user == "admin" and password == "1234":
    print("Accesso consentito")
# elif user != "admin" or password != "1234":
#     print("Accesso negato nell'elif") 
else:
    print("Accesso negato nell'else")
