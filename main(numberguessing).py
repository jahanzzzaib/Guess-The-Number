import random

number_list = list(range(1, 101))
number_to_guess = random.choice(number_list)

print('''
   ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \\
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/       
''')
print("Welcome to The Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

game_over = False
lives = 0
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5
else:
    print("Invalid input. Restart")
    exit()

while not game_over:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if lives <= 1:
        print("You're out of guesses, Re-run the code to play again.")
        game_over = True
    else:
        if guess == number_to_guess:
            print(f"You got it! The number was {number_to_guess}")
            game_over = True
        elif guess > number_to_guess:
            lives -= 1
            print("Too high")
        elif guess < number_to_guess:
            lives -= 1
            print("Too low")
