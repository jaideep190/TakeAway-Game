import random
import tkinter as tk
from tkinter import messagebox

def calculate_grundy(n):
    if n % 4 == 0:
        return 0
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n // 2
    else:
        return (n // 2) + 1

def computer_move(sticks):
    grundy_numbers = [calculate_grundy(sticks - i) for i in range(1, 4)]
    for i in range(3, 0, -1):
        if (sticks - i) >= 0:
            if calculate_grundy(sticks - i) == 0:
                return i
    return random.randint(1, min(sticks, 3))

def draw_sticks(num_sticks):
    sticks = "| " * num_sticks
    return sticks

def update_sticks():
    sticks_label.config(text=draw_sticks(sticks))

def player_turn(num):
    global sticks
    sticks -= num
    update_sticks()
    moves_list.insert(tk.END, f"You took {num} sticks")
    moves_list.see(tk.END)
    if sticks <= 0:
        messagebox.showinfo("Game Over", "Congratulations! You picked the last stick. You win!")
        root.destroy()
    else:
        computer_choice = computer_move(sticks)
        sticks -= computer_choice
        update_sticks()
        moves_list.insert(tk.END, f"Computer took {computer_choice} sticks")
        moves_list.see(tk.END)
        if sticks <= 0:
            messagebox.showinfo("Game Over", "Oops! Computer picked the last stick. Computer wins!")
            root.destroy()

def start_game():
    global sticks
    try:
        sticks = int(sticks_entry.get())
        if sticks < 1:
            messagebox.showerror("Error", "Please enter a valid number of sticks (greater than 0).")
        else:
            sticks_label.config(text=draw_sticks(sticks))
            sticks_entry.config(state="disabled")
            start_button.config(state="disabled")
            one_button.config(state="normal")
            two_button.config(state="normal")
            three_button.config(state="normal")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

sticks = 20
max_sticks = 50

root = tk.Tk()
root.title("Stick Game")

sticks_frame = tk.Frame(root)
sticks_frame.pack(pady=10)

sticks_label = tk.Label(sticks_frame, text=draw_sticks(sticks), font=("Courier", 12))
sticks_label.pack()

buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

one_button = tk.Button(buttons_frame, text="Take 1 Stick", command=lambda: player_turn(1), state="disabled")
one_button.grid(row=0, column=0, padx=5)

two_button = tk.Button(buttons_frame, text="Take 2 Sticks", command=lambda: player_turn(2), state="disabled")
two_button.grid(row=0, column=1, padx=5)

three_button = tk.Button(buttons_frame, text="Take 3 Sticks", command=lambda: player_turn(3), state="disabled")
three_button.grid(row=0, column=2, padx=5)

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

sticks_label = tk.Label(input_frame, text="Enter the number of sticks: ")
sticks_label.grid(row=0, column=0, padx=5)

sticks_entry = tk.Entry(input_frame)
sticks_entry.grid(row=0, column=1, padx=5)

start_button = tk.Button(input_frame, text="Start Game", command=start_game)
start_button.grid(row=0, column=2, padx=5)

moves_label = tk.Label(root, text="Moves Made:", font=("Helvetica", 10))
moves_label.pack(pady=(20, 5))

moves_list = tk.Listbox(root, width=50, height=20)
moves_list.pack()

# Adjust window size based on maximum number of sticks
window_width = len(draw_sticks(max_sticks)) * 10  # Adjust for stick width
window_height = 520
root.geometry(f"{window_width}x{window_height}")

root.mainloop()
