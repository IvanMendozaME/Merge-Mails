with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()
    print(names)

with open("Input/Letters/starting_letter.txt") as file:
    letter_target = file.read()

for i in names:
    letter_finals = letter_target.replace("[name]", i[0:len(i)-1] )
    with open(f"Output/ReadyToSend/LetterTo{i[0:len(i)-1]}.txt", "w") as file:
        file.write(letter_finals)

