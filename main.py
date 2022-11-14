import random


print("Infinity Dice 🎲.")
print()
print("""Roll a dice with any number of sides (essentially as big of a number as you like).""")
print()
print("Everytime you key in your response press enter.")

def rollDice():
  exit = ""
  while exit.lower() != "no" or exit.lower() != "no":
    print()
    try:
      num = int(input("How many sides?: "))
      print()
    except ValueError:
      print()
      print("I am expecting positive numbers.")
      print()
      continue
  
    if num <= 0:
      print("I don't like zero and negative numbers.")
      print("I am expecting positive integer numbers.")
      continue
    else:
      print("You rolled",random.randint(1,num))

     
    while exit.lower() != "yes":  
      exit = input("Roll again? ") 
      if exit.lower() == "no" or exit.lower() == "n":
        print()
        print("Thanks for playing Infinity Dice! 🎲")
        break
      elif exit.lower() == "yes" or exit.lower() == "y":
        break
      else:
        print()
        print("Am expecting 'yes' or 'no'; or 'y' or 'n' for yes and no respectively.")
        continue
      

def endGame():
  while True:
    print()
    input("""Thank you for playing!
To play again please click Stop on top right page and click Run to try again with a different number.""")
    print()
    continue


if __name__=="__main__":
  rollDice()
  endGame()