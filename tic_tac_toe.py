from tkinter import *
from tkinter import messagebox

# Game state
player = 'X'
game_over = False
states = [[0] * 3 for _ in range(3)]
buttons = [[0] * 3 for _ in range(3)]


def clicked(r, c):
    global player, game_over

    if states[r][c] != 0 or game_over: return

    # Place mark
    states[r][c] = player
    buttons[r][c].config(text=player)

    if check_win():
        messagebox.showinfo("Winner!", f"{player} wins!")
        game_over = True
        return

    if check_tie():
        messagebox.showinfo("Game Over", "It's a tie!")
        game_over = True
        return

    # Switch player
    player = 'O' if player == 'X' else 'X'


def check_win():
    # Rows
    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] != 0:
            return True

    # Columns
    for j in range(3):
        if states[0][j] == states[1][j] == states[2][j] != 0:
            return True

    # Diagonals
    if states[0][0] == states[1][1] == states[2][2] != 0:
        return True
    if states[0][2] == states[1][1] == states[2][0] != 0:
        return True
    return False


def check_tie():
    return all(states[i][j] != 0 for i in range(3) for j in range(3))


# Setup window
root = Tk()
root.title("Bhavik's: Tic Tac Toe")
root.resizable(0, 0)

# Create buttons
for i in range(3):
    for j in range(3):
        buttons[i][j] = Button(root, height=4, width=8, font=("Helvetica", 20),
                               command=lambda r=i, c=j: clicked(r, c))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()
