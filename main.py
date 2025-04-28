import json
#
# Odczytywanie
# Opening JSON file
#with open('Slownik.json', 'r') as openfile:
#	# Reading from json file
#	slownik = json.load(openfile)
#
#print(slownik)
#
#noweimie = input("Jakie imię chcesz dodać? : ")
#nowaocena = input("Jaką ocenę otrzymała ta osoba? : ")
#
#slownik[noweimie] = nowaocena
#
#print(slownik)
#
#ocenadousuniecia = input("Jakiego ucznia (z oceną) chcesz usunąć? : ")
#
#slownik.pop(ocenadousuniecia)
#
# Tworzenie słownika
#Json_object = json.dumps(slownik, indent = 4)
#
# Owieranie pliku jako outfile
#with open("Slownik.json","w") as outfile:
#	outfile.write(Json_object)
#--------------------------------------
#wpisz:
#1 - wyswietl
#2 - dodaj
#3 - usun
#4 - zapisz i wyjdz

# Otwieranie
with open('Slownik.json', 'r') as openfile:
    # Reading from json file - Czytanie
    slownik = json.load(openfile)

while True:
    opcja = input('''Wybierz opcję: 
    1 - wyswietl
    2 - dodaj
    3 - usun
    4 - zapisz i wyjdz''')
    if opcja == '1':
        print(slownik)
    elif opcja == '2':
        noweimie = input("Jakie imię chcesz dodać? : ")
        nowaocena = input("Jaką ocenę otrzymała ta osoba? : ")
        slownik[noweimie] = nowaocena
    elif opcja == '3':
        uczendousuniecia = input("Jakiego ucznia (z oceną) chcesz usunąć? : ")
        if uczendousuniecia in slownik:
            slownik.pop(uczendousuniecia)
        else:
            continue
    elif opcja == '4':
        # Tworzenie słownika
        Json_object = json.dumps(slownik, indent=4)
        # Owieranie pliku jako outfile
        with open("Slownik.json", "w") as outfile:
            outfile.write(Json_object)
    else:
        break
    break
