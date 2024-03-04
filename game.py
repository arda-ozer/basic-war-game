import random
import sys

player_health = 100
ai_health = 100
IsgameWorking = True

prefer = input("Please type Y or T  !! Please use only uppercase !!  ")

myList = ["Y","T"]

starter = random.choice(myList)

if starter == prefer:
    print("You will start the game first !!")
    player_turn = True

elif starter != prefer:
    print("A.I will start the game first !!")
    player_turn = False   

while IsgameWorking is True:
 if player_health <= 0:
  print("The A.I has won the game !!!")
  IsgameWorking = False

 elif ai_health <= 0:
  print("The player has won the game !!!")
  IsgameWorking = False
 
 else:

  while player_turn is True: # Player's move
     print("                  ")
     print("**** PLAYER'S TURN ****")

     action = input("Please choose your next move 1:attack 2:defend 3:exit ")
     match action:
        case "1":
         damage = random.randint(1,20)
         ai_health = ai_health - damage
         print("You've inflicted ",damage," damage, A.I has ",ai_health," health points now")
         player_turn = False
        case "2":
          defence = random.randint(1,5)
          player_health = player_health + defence
          print("Your health has been increased by ",defence," points, now you have ",player_health," health points") 
          player_turn = False
        case "3":
          sys.exit("The player has left the game, The A.I has won the game !!!")
 
  while player_turn is False: # A.I's move
     
     if ai_health <= 10:
      exit_rate = random.randint(0,10)
      lucky_num = random.randint(0,10)

      if exit_rate <= lucky_num:
         sys.exit("The A.I has left the game, The player has won the game !!! ")
      else:
         player_turn = False
     else:

      print("                  ") 
      print("**** A.I'S TURN ****")

     action = random.randint(1,2)

     match action:
       case 1:
         damage = random.randint(1,20)
         player_health = player_health - damage
         print("The A.I has inflicted ",damage," damage, player now has ",player_health," health points")
         player_turn = True
       case 2:
         defence = random.randint(1,10)
         ai_health = ai_health + defence
         print("A.I has increased its health by ",defence," points, now it has ",ai_health," health points")
         player_turn = True   
      



