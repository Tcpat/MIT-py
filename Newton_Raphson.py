y = int(input("Enter a positive integer")
epsilon = 0.001
guess = y / 2.0
numGuesses = 0

while abs(guess**2 - y) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2) - y) / (2*guess))

print("Number of guesses was ", numGuesses)
print("Square root of ", y, " is about ", guess)
