import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output = [phonetic_dict[alpha] for alpha in word]
    except KeyError:
        print("Sorry, only letters in the alphabet are allowed.")
        generate_phonetic()
    else:
        print(output)

generate_phonetic()