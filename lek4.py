# en slumpgenerator
# program som rullar en tärning

import random

print("Vill du rulla tärning?")


try:
    sides = int(input("Hur många sidor?"))
except:
    print("Tärningen behöver 1+ sidor")
    sides = 1

run = "y"

while run.lower() == "y":   
    randomNumber = random.randint(1, sides)
    print(randomNumber)

    run = input("Vill du rulla en till tärning Y/N ")