print("Program Liczący średnię ocene z opcją dodawania ocen po wyświetleniu średniej.\nOceny z wagą 3:\n(Wpicz 0 gdy skończysz)")
spr=[]##waga3 tablica
while 0 == 0:
    spr += [int(input())]
    if(spr[-1]==0):
        spr.pop(-1)
        break
print(spr)

##Sprawdziany
print("Oceny z wagą 2:\n(Wpicz 0 gdy skończysz)")
kart=[]##waga 2 tablica
while 0 == 0:
    kart += [int(input())]
    if(kart[-1]==0):
        kart.pop(-1)
        break
print(kart)

##Odpowiedz
print("Oceny z wagą 1:\n(Wpicz 0 gdy skończysz)")
odp=[]##waga 1 tablica
while 0 == 0:
    odp += [int(input())]
    if(odp[-1]==0):
        odp.pop(-1)
        break
print(odp)

##obliczenia
sumaspr = 0
sumakart = 0
sumaodp = 0
for a in spr:
    sumaspr += a
for b in kart:
    sumakart += b
for c in odp:
    sumaodp += c
    
sumaspr = sumaspr*3
sumakart = sumakart*2
suma = sumaspr + sumakart + sumaodp
locen = (len(spr)*3) + (len(kart)*2) + len(odp)
ocena = suma/locen

##wypicywanie oceny
print("Twoja ocena to:")
print(ocena)
##wpisywanie dodatkowych ocen

while 0==0:
 print('Sprawdz średnią z dodatkową oceną \nJeśli chcesz dodawać ocene wpisz (+) Jeśli chcesz odejąć ocene wpisz(-)\nWyjście (0)')
 dzial = input()
 if dzial=='+':
    while 0==0:
          print('Ocena:\nJeśli nie chcesz wpisz (0)')
          Docena = int(input())
          if Docena ==0:
              break
          print ('Waga:\nJeśli nie chcesz wpisz (0)')
          Dwaga = int(input())

          suma =suma +  (Docena*Dwaga)
          locen =locen + Dwaga
  
          ocena = suma/locen
          print("Twoja ocena z dodatkową oceną:")
          print(ocena)
  
 if dzial=='-':
    while 0==0:
          print('Ocena:\nJeśli nie chcesz wpisz (0)')
          Docena = int(input())
          if Docena ==0:
             break
          print ('Waga:\nJeśli nie chcesz wpisz (0)')
          Dwaga = int(input())
          suma = suma -  (Docena*Dwaga)
          locen = locen - Dwaga
          
          ocena = suma/locen
          print("Twoja ocena z odjętą oceną:")
          print(ocena)
          
 if  dzial == '0':  
   print('Dziękuję za skorzystanie z programu do liczenia średniej ocen\n Twoja średnia to:')
   print(ocena)
   break

