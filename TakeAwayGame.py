from math import gcd

def mex(numbers):
    """
    Minimum Excluded Value (mex) function.
    Returns the smallest non-negative integer not present in the input set.
    """
    seen = set()
    i = 0
    while True:
        if i not in numbers:
            return i
        seen.add(i)
        i += 1

def grundy(n):
    """
    Calculate the Grundy value of a given pile size using the Sprague-Grundy theory.
    """
    if n == 0:
        return 0
    values = set()
    for i in range(1, n + 1):
        values.add(grundy(n - i))
    return mex(values)

def play_game():
    """
    Play the Take Away Sticks game.
    """
    sticks = int(input("Enter the number of sticks: "))
    total_grundy = grundy(sticks)

    player_turn = True
    while sticks > 0:
        if player_turn:
            print(f"Player's turn. Sticks remaining: {sticks}")
            move = int(input("Enter the number of sticks to remove (1-3): "))
            if move < 1 or move > 3 or move > sticks:
                print("Invalid move. Try again.")
                continue
            sticks -= move
        else:
            computer_grundy = grundy(sticks)
            move = (total_grundy ^ computer_grundy)
            if move == 0:
                move = 1
            print(f"Computer removed {move} sticks.")
            sticks -= move

        player_turn = not player_turn

    if player_turn:
        print("Congratulations! You won!")
    else:
        print("Sorry, you lost. The computer won.")

play_game()