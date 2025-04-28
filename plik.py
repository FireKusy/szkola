import json
slownik = { 'Ola':'5', 'Pola':'4', 'Tola':'3'}

n = input("Jakie imię chcesz dodać? : ")
m = input("Jaką ocenę otrzymała ta osoba? : ")

slownik[n] = m

print(slownik)

Json_object = json.dumps(slownik, indent = 4)

# Pisanie
with open("Slownik.json","w") as outfile:
	outfile.write(Json_object)

# Opening JSON file - Otwieranie
with open('Slownik.json', 'r') as openfile:
	# Reading from json file - Czytanie
	czytanyslownik = json.load(openfile)

print(czytanyslownik)
