import random
import day12_art

answer = random.randint(1,100)

def guess_the_game():
    global attempts
    game_over = False
    while attempts > 0 and not game_over :
        print(f"You have {attempts} attempts remaining to guess the number")
        guess = int(input("Guess a number: "))
            
        if guess == answer:
            game_over = True
            print (f"You got it!. The answer was {guess}") 
        elif guess > answer:
            print ("Too high!")
            attempts -=1
        elif guess < answer:
            print ("Too low!")
            attempts -=1
        
        if guess != answer and attempts != 0:
            print("Guess again.")
            
        
        if attempts == 0:
            print("You've run out of guesses! Refresh the page to run again")

print(day12_art.logo)
print("Welcome to the Number Guessing game")
print("I am thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty: 'easy' or 'hard': ").lower()
if difficulty == "easy":
    attempts = 10
    guess_the_game()
elif difficulty == "hard":
    attempts = 5
    guess_the_game()

















