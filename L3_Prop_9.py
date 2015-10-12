print("Please think of a number between 0 and 100!")
low = 0
high = 100
guessed = False
while not guessed:
    guess = (high + low) / 2
    print('Is your secret number ' + str(guess) + '?')
    human_input = raw_input('Enter "h" to indicate the guess is too high. Enter "l" to\
    indicate the guess is too low. Enter "c" to indicate I guessed correctly. ')
    if human_input == "c":
        print('Game over. Your secret number was: ' + str(guess))
        guessed = True
    elif human_input == "h":
        high = guess
    elif human_input == "l":
        low = guess
    else:
        print("Sorry, I did not understand your input.")