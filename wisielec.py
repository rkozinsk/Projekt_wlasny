import sys

nr_of_tries = 5
word = 'katakumby'
used_letters = []

user_word = []

def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes

for _ in word:
    user_word.append('_')

while True:
    letter = input('Podaj literę')
    used_letters.append(letter) # dodaje literą z input do listy

    found_indexes = find_indexes(word, letter)

    if len(found_indexes) == 0:
        print("Nie ma takiej litery.")
        nr_of_tries -=1
        print("pozostało prór:", nr_of_tries)

        if nr_of_tries == 0:
            print('Koniec gry : przegrałeś :(')
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter


    print('Użyte litery:', used_letters)
