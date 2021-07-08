


import art
import random
print(art.logo)

computer = random.randint(1,100)

print("Im Guessing a Number between 1 to 100 \n")

start = True
while start:
  mode = input("Type Mode : Easy (10 Attempts) or Hard (5 Attempts): ").lower()
  if mode == "easy":
    attempts = 10
  else : 
    attempts = 5
  while attempts !=0:
    user_guess = int(input("Guess the number\n"))
    if user_guess == computer:
      print(f"You got it on {attempts} attempt")
    elif user_guess > computer:
      attempts -= 1
      print(f"Too high \nYou are having {attempts} attempt")    
    elif user_guess < computer:
      attempts -= 1
      print(f"Too low \nYou are having {attempts} attempt")
  if attempts == 0:
    print(f"You Lost The Number is {computer}")
  if input("To Restart the game 'Y'\nTo Quit 'N'\n").lower()  == "n":
    start = False      