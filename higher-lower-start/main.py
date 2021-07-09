from replit import clear
import random
import art
import game_data

play = True
UserB = random.choice(game_data.data)

def check_folowers(UserA, UserB):
  if UserA["follower_count"] > UserB["follower_count"]:
    print("you are Right")
    return True
  else : 
    print("you are wrong")
    return False

score=0

while play :
  clear()
  print(art.logo)
  UserA = UserB
  while UserA == UserB:
    UserB = random.choice(game_data.data)
  if score != 0:
    print(f"Your Score : {score}")
  print(f"Compare A : {UserA['name']}, {UserA['description']}, from country {UserA['country']}")
  print(art.vs)
  
  print(f"Compare B : {UserB['name']}, {UserB['description']}, from country {UserB['country']}")
  print("Who has more followers ? ")
  high = ""
  while high !="A" and high != "B":
    high = input("type 'A' or 'B' : ").upper()
    if high == 'A':
      play = check_folowers(UserA, UserB)
      if play:
        score += 1
    elif high == 'B':
      play = check_folowers(UserB, UserA)
      if play:
        score += 1
    else:
      print("Enter valid Choice : ")    
  


    

