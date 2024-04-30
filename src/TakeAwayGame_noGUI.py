import random

def calculate_grundy(n):
    # Function to calculate the Grundy number for a given number of sticks
    if n % 4 == 0:
        return 0
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n // 2
    else:
        return (n // 2) + 1

def computer_move(sticks):
    # Computer's move based on Sprague-Grundy strategy
    grundy_numbers = [calculate_grundy(sticks - i) for i in range(1, 4)]
    for i in range(3, 0, -1):
        if (sticks - i) >= 0:
            if calculate_grundy(sticks - i) == 0:
                return i
    return random.randint(1, min(sticks, 3))

def main():
    sticks = int(input("Enter the number of sticks: "))
    player_turn = True

    while sticks > 0:
        print(f"\nRemaining sticks: {sticks}")

        if player_turn:
            player_choice = int(input("How many sticks do you want to take (1, 2, or 3)? "))
            if player_choice < 1 or player_choice > 3 or player_choice > sticks:
                print("Invalid choice. Please choose 1, 2, or 3 sticks.")
                continue
            sticks -= player_choice
            if sticks <= 0:
                print("You win! You picked the last stick.")
                break
            player_turn = False
        else:
            computer_choice = computer_move(sticks)
            print(f"Computer takes {computer_choice} sticks.")
            sticks -= computer_choice
            if sticks <= 0:
                print("Computer wins! computer picked the last stick.")
                break
            player_turn = True

if __name__ == "__main__":
    main()
