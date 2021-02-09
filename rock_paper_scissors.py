from random import randint
choice = ["rock","paper","scissors"]
random_number = randint(0,2)
random_choice = choice[random_number]
print(random_choice)
player = False

while (player == False):
      player = input()
      if(player == random_choice):
          print("TIE MATCH")
      elif(player == "rock"):
          if(random_choice == "paper"):
              print("You Lose",random_choice,"covers",player)
          else:
              print("You Win",player,"covers",random_choice)
      elif(player == "paper"):
          if(random_choice == "rock"):
              print("You Win",player,"destroyes",random_choice)
          else:
              print("You Lose",random_choice,"covers",player)
      elif(player == "scissors"):
          if(random_choice == "rock"):
              print("You Lose",random_choice,"beats",player)
          else:
              print("You Win",player,"beats",random_choice)
      else:
          print("Invalid entry")
      if(player == "exit"):
          print("EXiting")
          break
      player = False
      random_number = randint(0,2)
      random_choice = choice[random_number]
