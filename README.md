 # Temat: Dziennik z ocenami uczniów.
 Piotr Kusiński 2a1

 Projekt polega na aplikacji w pythonie, edytujący słownik w jsonie, który jest odczytywany i powstał na podstawie wpisanego słownika w pierwszym pliku.
 Aplikacja daje wybór: wyświetlania słownika uczniów, dodawania nowego ucznia z oceną, usuwania ucznia na podstawie imienia lub zapisania i wyjścia z niej.
 (W razie usuwania według imienia nieznajdującego się w liście aplikacja pomija krok i pokazuje menu aplikacji ponownie).

 # Na początku projekt powstawał według tego pliku (plik.py):

 import json
 slownik = { 'Ola':'5', 'Pola':'4', 'Tola':'3'}

 n = input("Jakie imię chcesz dodać? : ")
 m = input("Jaką ocenę otrzymała ta osoba? : ")

 slownik[n] = m

 print(slownik)

 Json_object = json.dumps(slownik, indent = 4)

 with open("Slownik.json","w") as outfile:
	outfile.write(Json_object)

 - Opening JSON file
 with open('Slownik.json', 'r') as openfile:
	- Reading from json file
	czytanyslownik = json.load(openfile)

 print(czytanyslownik)

 Run:

 Podajemy dla przykłady imię Ania z oceną 4:

 Jakie imię chcesz dodać? : Ania
 Jaką ocenę otrzymała ta osoba? : 4
 {'Ola': '5', 'Pola': '4', 'Tola': '3', 'Ania': '4'}
 {'Ola': '5', 'Pola': '4', 'Tola': '3', 'Ania': '4'}

 Plik w formacie json wygląda tak(Slownik.json):

 {
     "Ola": "5",
     "Pola": "4",
     "Ania": "4"
 }

 Następnie tworzę kolejny plik (main.py), odczytywujący plik json i tworzący aplikację, która daje opcje do wyboru, dotyczące operowania aplikacji:

 import json

 with open('Slownik.json', 'r') as openfile:
     - Reading from json file
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
         ocenadousuniecia = input("Jakiego ucznia (z oceną) chcesz usunąć? : ")
         if ocenadousuniecia in slownik:
             slownik.pop(ocenadousuniecia)
         else:
             continue
     elif opcja == '4':
         - Tworzenie słownika
         Json_object = json.dumps(slownik, indent=4)
         - Owieranie pliku jako outfile
         with open("Slownik.json", "w") as outfile:
              outfile.write(Json_object)
         break

 Plik json (Slownik.json) po zedytowaniu się zmienia na podstawie dodawania, usuwania lub zapisywania tej w aplikacji.