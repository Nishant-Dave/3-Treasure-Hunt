print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


choice1 = input("Which side you want to go? Left or Right? \n").lower()
if choice1 == "right":
  choice2 = input(
      "There's a huge montain infront of you. Would you climb the mountain or will go through the cave? Climb or Cave? \n"
  ).lower()
  if choice2 == "climb":
    choice3 = input(
        "There's a big ground and you will need a ride. What will you choose? Horse or Bear \n"
    ).lower()
    if choice3 == "horse":
      choice4 = input(
          "Wow, finally you reached the Castle! but it has 3 doors. choose wisely. Blue, Yellow or Red \n"
      ).lower()
      if choice4 == "yellow":
        print(
            "Congratulations!!! The treasure is yours.\n 💎💍💎🪙💍💎💍🏆🪙💎💍💎💎🪙💍🏆🪙💍💎🪙💎🪙🪙"
        )
      elif choice4 == "blue":
        print("The room is filled with beasts, Game Over")
      elif choice4 == "red":
        print("Danger! It is fire. Game Over")
      else:
        print("This door doesn't exist. Game Over")
    elif choice3 == "bear":
      print("You messed with bear. Game Over")
    else:
      print("There's no such animal available. Game Over")
  elif choice2 == "cave":
    print("Wrong decision. Cave is full of deadly animals. Game Over")
  else:
    print("There no where else to go. Game Over.")
elif choice1 == "left":
  print("Why did you go Left? It's a cliff. Game Over")
else:
  print("You had only 2 options. Sorry Game Over.")
