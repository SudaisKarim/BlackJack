############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
total_value2 = 0
import random
import art 
print(art.logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10,]


yes_no = input("HELLO, would for me to deal a card? y/n ")
if yes_no == "y":
  first_card = (random.choice(cards))
  print(f"Your first card is {first_card}")
else:
  print("ok")

robot_first_card = (random.choice(cards))
print(f"The robot's first card is {robot_first_card}")


yes_no2 = input("Would you like me to deal another card? y/n ")
if yes_no2 == "y":
  second_card = (random.choice(cards))
  total_value = (int(second_card + first_card))
  print(f"You are now at...\n {total_value}")
else:
  print("ok")

robot_second_card = (random.choice(cards))
print(f"Now for the robot's turn... \n The robot's second card is hidden but you know that the robot's first card was: {robot_first_card}")
robot_total_card_value = robot_first_card + robot_second_card


yes_no2 = input("Would you like me to deal another card for you? y/n ")
if yes_no2 == "y":
  third_card = (random.choice(cards))
  print("You are now at...")
  total_value2 = int(first_card) + int(second_card) + int(third_card)
  print(total_value2)
  if total_value2 > 21:
    print("YOU LOST, YOU CAN'T GO OVER 21, UNLUCKY")
  print(f"And the robot's card value is {robot_total_card_value}")
  if int(total_value2) > int(robot_total_card_value):
    print("YOU WIN")
  elif int(total_value2) < int(robot_total_card_value):
    print("YOU LOSE")
  elif int(total_value2) == int(robot_total_card_value):
    print("TIE")
    exit()
else:
  print(f"Ok, your card value is {total_value}")
  print(f"And the robot's total card value is {robot_total_card_value}")
  if int(total_value) > int(robot_total_card_value):
    print("YOU WIN")
  elif int(total_value) < int(robot_total_card_value):
    print("YOU LOSE")
  elif int(total_value) == int(robot_total_card_value):
    print("TIE")

  



