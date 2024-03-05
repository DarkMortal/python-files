import random
import os
import platform

def clearScreen():
    operating_system = platform.system()
    if operating_system == "Linux":
        os.system("clear")
    elif operating_system == "Windows":
        os.system("cls")

options = ["Rock", "Paper", "Scissors"]

if __name__ == "__main__":
    userWin = 0
    computerWin = 0

    while True:
        clearScreen()
        print(f"User win count: {userWin}\nComputer win count: {computerWin}\n")

        for index in range(len(options)):
            print(f"{index + 1}. {options[index]}")
        playerB = "" # user

        while playerB == "":
            try:
                playerB = int(input("\nMake a choice: "))
                if playerB < 1 or playerB > 3:
                    raise ArithmeticError("Choice can't be less than 1 or greater than 3")
            except ArithmeticError as exc:
                print(str(exc))
                playerB = ""
            except Exception:
                print("Please enter a valid choice")
                playerB = ""

        playerA = random.randint(1, 3) # computer
        print(playerA)
        print(f"User choice: {options[playerB - 1]}\nComputer choice: {options[playerA - 1]}")

        if playerA == playerB: print("Tie")
        elif (playerA + 1) % 3 == playerB % 3:
            print("User wins")
            userWin += 1
        else:
            print("Computer wins")
            computerWin += 1

        choice = input("Would you like to continue playing? (Y/N)")[0]
        if choice == 'Y' or choice == 'y': continue
        else: break