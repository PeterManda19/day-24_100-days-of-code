import random


print("Infinity Dice 🎲.")
print()
print("""Roll a dice with any number of sides (essentially as big of a number as you like).""")
print()
print("Everytime you key in your response press enter.")

def promptUser():
  while True:
    print()
    try:
      num = int(input("How many sides?: "))
      print()
      return num
    except ValueError:
      print()
      print("I am expecting positive numbers.")
      print()
      continue  
    if num <= 0:
      print("I don't like zero and negative numbers.")
      print("I am expecting positive integer numbers.")
      continue


def rollDice(num):
    print("You rolled",random.randint(1,num))

def quit():
  exit = ""
  while exit.lower() != "no" or exit.lower() != "n":  
    exit = input("Roll again? ") 
    if exit.lower() == "yes" or exit.lower() == "y" or exit =="":
      num = promptUser()
      rollDice(num) 
    else:
     print()
     print("Shutting down Infinity Dice 🎲...")
     break
      

def endGame():
  while True:
    print()
    input("""Thank you for playing!
To play again please click Stop on top right page and click Run to try again with a different number.""")
    print()
    continue


if __name__=="__main__":
  num = promptUser()
  rollDice(num)
  quit()
  endGame()