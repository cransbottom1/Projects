from time import sleep
from random import randint

asterisks = "*" * 14
for stars in range(14):
    print(asterisks[stars], sep='', end='', flush=True), sleep(0.10)

title = "\n*Dice Roller *"

for characters in range(15):
    print(title[characters], sep='', end='', flush=True), sleep(0.10)

asterisks = "\n**************"
for stars in range(15):
    print(asterisks[stars], sep='', end='', flush=True), sleep(0.10)

sleep(1)

print("\n")

roller = True

counter = 0

instructions = input("Welcome to Dice Roller!\n"
                     "Enter 'q' to quit at any time.\n"
                     "Enter 'c' to continue.\n"
                     "\n"
                     ">")

if instructions == 'c':
    roller = True
    while roller:
        die_selection = input("\nEnter 'q' at any time to quit.\n\n"
                              "Enter '6' for a d6.\n"
                              "Enter '10' for a d10.\n"
                              "Enter '20' for a d20.\n"
                              "\n"
                              ">")
        if die_selection == 'q':
            roller = False
            print("Thanks for trying Dice Roller!")
        elif die_selection == '6':
            d6 = (randint(1, 6))
            print(f"you rolled {d6}.")
        elif die_selection == '10':
            d10 = (randint(1, 10))
            print(f"You rolled {d10}.")
            print()
        elif die_selection == '20':
            d20 = (randint(1, 20))
            print(f"You rolled {d20}.")
            print()
        elif die_selection == '':
            print("Please make a selection.")
        else:
            print("No die of that type")
