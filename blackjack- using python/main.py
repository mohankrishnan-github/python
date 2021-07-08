from replit import clear
import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def handle_cards():
  l = []
  l.append(random.choice(cards))
  l.append(random.choice(cards))
  return l

def check_blackJack(uDeck, dDeck):
  if sum(uDeck) == 21 or sum(dDeck) == 21:
    return True
  else:
    return False   

def hit(uDeck ,dDeck):
  uSum = sum(uDeck)
  dSum = sum(dDeck)  
  while dSum <= 17:
    dDeck = stand(dDeck)
    dSum = sum(dDeck)
  if uSum ==  dSum:
      print("Its Draw")
  elif uSum > 21:
    print(f"{uDeck} = {uSum} You Bust , Dealer Win's")
    return
  elif dSum > 21:
    print(f"{dDeck} = {dSum} Dealer Bust , You Win")  
    return
  elif uSum > dSum:
    print(f"{uDeck} = {uSum} You Win")
  else :
    print(f"{dDeck} = {dSum} Dealer Win's")  

def stand(deck):
  deck.append(random.choice(cards))
  return deck


userChoice = input("'Y' to PLay 'N' to Quit : ").lower()
while userChoice != "n":
  print(art.logo)
  user_deck = handle_cards()
  dealer_deck = handle_cards()
  print(f"Your Deck : {user_deck}\nDealer's first one : {dealer_deck[0]}")

  choice = input("Hit or Stand\n'H' for Hit 'S' for Stand : " ).lower()
  while choice != "h" and sum(user_deck) <= 21 :
    user_deck = stand(user_deck)
  if check_blackJack(user_deck, dealer_deck):
    print("Its BlackJack")   
  else:
    hit(user_deck, dealer_deck) 
  userChoice = input("'Y' To Continue 'N' to Quit : ").lower()
  clear()

