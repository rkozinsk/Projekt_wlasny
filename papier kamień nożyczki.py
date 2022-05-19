import getpass

gracz1_wynik = 0
gracz2_wynik = 0
remiy = 0

opcje = ['kamień', 'papier', 'nożyczki']
print("opcje do wyboru", opcje)

def pobierz_wybor(gracz):
    while True:
        wybor_gracza = getpass.getpass(f'{gracz} \n podaj swój wybór: ')
        if wybor_gracza in opcje:
            return wybor_gracza

while gracz1_wynik != 3 and gracz2_wynik != 3:
    wybor_gracza1 = pobierz_wybor('Gracz1')
    wybor_gracza2 = pobierz_wybor('Gracz2')

    if wybor_gracza1 == 'papier' and wybor_gracza2 == 'kamień'\
    or wybor_gracza1 == 'kamień' and wybor_gracza2 == 'nożyczki'\
    or wybor_gracza1 == 'nożyczki' and wybor_gracza2 == 'papier':
        print('\n Gracz 1 \n WYGRAŁ \n')
        gracz1_wynik += 1
    elif wybor_gracza1 == wybor_gracza2:
        print("\n REMIS \n")
        remiy +=1
    else:
        print('\n Gracz 2 \n WYGRAŁ \n')
        gracz2_wynik += 1
    print('Gracz 1 wybrał:', wybor_gracza1, ',a Gracz 2 wybrał:', wybor_gracza2)

if gracz1_wynik > gracz2_wynik:
    print('-----------------------\n Gracz1 \n WYGRAŁ całą grę\n -----------------------')
else:
    print('-----------------------\n Gracz2 \n WYGRAŁ całą grę\n -----------------------')


print('Gracz 1 wygrał', gracz1_wynik, 'razy, a Gracz 2 wygrał', gracz2_wynik, 'razy, remisów było', remiy)
