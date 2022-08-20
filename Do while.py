secret_word = "hi"
counter = 0

while True:
    word = input("Writ hi : ").lower()
    counter = counter + 1
    if word == secret_word:
        break
    if word != secret_word and counter > 4:
        break