with open("./Input/Names/invited_names.txt") as f:
    names = f.readlines()

with open("./Input/Letters/starting_letter.txt") as f:
    letter = f.read()

for name in names:
    with open(f"./Output/ReadyToSend/letter_to_{name.strip()}.txt", "w") as f:
        temp_letter = letter.replace("[name]", name.strip())
        f.write(temp_letter)


