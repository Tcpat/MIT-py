input("Please think of a number between 0 and 100!")
answer = ""
low = 1
high = 100
number = int((low + high) / 2)
while answer != "c":
    print("Is your secret number ", number, "?")
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if answer == "h":
        high = number
        number = int((low + high) / 2)
    elif answer == "l":
        low = number
        number = int((low + high) / 2)
    elif answer == "c":
        break
    else:
        print("try again")
print("Game over. Your secret number was: ", number)
