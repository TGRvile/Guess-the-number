import random

Number1to10 = random.randint(1, 10)
print('hint the number is', Number1to10)
try:
    input1 = int(input("guess the number 1 to 10: "))
except ValueError:
    print("This isnt a number in number form")
    exit()
if Number1to10 == input1:
    print("you guessed the number!")
else:
    print("incorect guess")
