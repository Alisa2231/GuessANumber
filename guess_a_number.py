import random

print("Let's play the game 'Guess A Number'!")
random_number = random.randint(1, 100)
print("The computer has generated a random number between 1 and 100 inclusive, you have to guess it!")

player_guess = input("Guess the number: ")
while not player_guess.isdigit():
    print("Invalid input, the game works with numbers only.")
    player_guess = input("Guess the number: ")
player_guess = int(player_guess)
attempts = 1
while player_guess != random_number:
    if player_guess < random_number:
        print(f"Your guess {player_guess} is smaller than the number.")
    else:
        print(f"Your guess {player_guess} is bigger than the number.")
    player_guess = input("Guess again: ")
    while not player_guess.isdigit():
        print("Invalid input, the game works with numbers only.")
        player_guess = input("Guess again: ")
    player_guess = int(player_guess)
    attempts += 1

print(f"Congratulations, you guessed the number {random_number} in {attempts} attempts!")
