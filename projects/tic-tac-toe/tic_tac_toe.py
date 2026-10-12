import tkinter as tk
import random

current_player = 'X'
ai_is_on = True
ai_difficulty = 'Easy'
ai_is_next = True
turn_counter = 0

# Board Buttons
def player_turn(row, col, board):
    global current_player
    global ai_is_on
    global ai_is_next
    global turn_counter
    pvp_button.config(state='disabled')
    pvc_button.config(state='disabled')
    easy_button.config(state='disabled')
    medium_button.config(state='disabled')
    hard_button.config(state='disabled')
    button = board[row][col]
    turn_counter += 1
    button.config(text=current_player, state='disabled')
    if turn_counter >= 5:
        is_winner =check_winner()
        if is_winner:
            turn_label.config(text=f"{current_player} wins!")
            for r in range(3):
                for c in range(3):
                    board_buttons[r][c].config(state='disabled')
            return
    if turn_counter == 9:
        turn_label.config(text="It's a tie!")
        return
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'
    turn_label.config(text=f"{current_player}'s turn")
    if ai_is_on and ai_is_next:
        ai_is_next = False
        ai_turn()
    else:
        ai_is_next = True

# AI Logic

def set_difficulty(level):
    global ai_difficulty
    ai_difficulty = level

def ai_turn():
    global ai_difficulty
    empty_buttons = [(r, c) for r in range(3) for c in range(3) if board_buttons[r][c]['text'] == '']
    if ai_difficulty == 'Easy':
        # Easy AI: Randomly pick an empty spot
        if empty_buttons:
            row, col = random.choice(empty_buttons)
    elif ai_difficulty == 'Medium':
        # Medium AI: Randomly pick an empty spot, but also check for blocking moves
        # This is a placeholder for a more complex AI algorithm
        possible_block = check_block()
        row, col = 3, 3 # Default to an invalid move
        while (row, col) not in empty_buttons and empty_buttons:
            if possible_block!=[] and empty_buttons:
                row, col = random.choice(possible_block)
            else:
                row, col = random.choice(empty_buttons)
    elif ai_difficulty == 'Hard':
        # Hard AI: Implement a simple strategy (e.g., win if possible, block opponent)
        possible_win = check_win()
        row, col = 3, 3 # Default to an invalid move
        while (row, col) not in empty_buttons and empty_buttons:
            if possible_win!=[] and empty_buttons:
                row, col = random.choice(possible_win)
            else:
                possible_block = check_block()
                if possible_block!=[] and empty_buttons:
                    row, col = random.choice(possible_block)
                elif empty_buttons:
                    row, col = random.choice(empty_buttons)
    player_turn(row, col, board_buttons)

def check_block():
    opponent = [(r, c) for r in range(3) for c in range(3) if board_buttons[r][c]['text'] == 'X']
    computer = [(r, c) for r in range(3) for c in range(3) if board_buttons[r][c]['text'] == 'O']
    line_left = [] # This will hold potential blocking moves
    for (r, c) in opponent:
        # Check rows and columns for a potential block
        for i in range(3):
            if (r, i) not in opponent and (r, i) not in computer and all((r, j) in opponent for j in range(3) if j != i):
                line_left.append((r, i))
            if (i, c) not in opponent and (i, c) not in computer and all((j, c) in opponent for j in range(3) if j != i):
                line_left.append((i, c))
        # Check diagonals for a potential block
        for i in range(3):
            if (i, i) not in opponent and (i, i) not in computer and all((k, k) in opponent for k in range(3) if k != i):
                line_left.append((i, i))
            if (i, 2 - i) not in opponent and (i, 2 - i) not in computer and all((k, 2 - k) in opponent for k in range(3) if k != i):
                line_left.append((i, 2 - i))
    return line_left

def check_win():
    # This function would check the board for a win condition and return True if there's a winner
    opponent = [(r, c) for r in range(3) for c in range(3) if board_buttons[r][c]['text'] == 'X']
    computer = [(r, c) for r in range(3) for c in range(3) if board_buttons[r][c]['text'] == 'O']
    line_left = [] # This will hold potential winning moves
    for (r, c) in computer:
        # Check rows and columns for a potential win
        for i in range(3):
            if (r, i) not in opponent and (r, i) not in computer and all((r, j) in computer for j in range(3) if j != i):
                line_left.append((r, i))
            if (i, c) not in opponent and (i, c) not in computer and all((j, c) in computer for j in range(3) if j != i):
                line_left.append((i, c))
        # Check diagonals for a potential win
        for i in range(3):
            if (i, i) not in opponent and (i, i) not in computer and all((k, k) in computer for k in range(3) if k != i):
                line_left.append((i, i))
            if (i, 2 - i) not in opponent and (i, 2 - i) not in computer and all((k, 2 - k) in computer for k in range(3) if k != i):
                line_left.append((i, 2 - i))
    return line_left

# Check for winner and reset game functions
def check_winner():
    # This function would check the board for a winner and update the game state accordingly
    global board_buttons
    global current_player
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board_buttons[i][0]['text'] == board_buttons[i][1]['text'] == board_buttons[i][2]['text'] != '':
            for c in range(3):
                board_buttons[i][c].config(bg='lightgreen')
            return True
        if board_buttons[0][i]['text'] == board_buttons[1][i]['text'] == board_buttons[2][i]['text'] != '':
            for r in range(3):
                board_buttons[r][i].config(bg='lightgreen')
            return True
    if board_buttons[0][0]['text'] == board_buttons[1][1]['text'] == board_buttons[2][2]['text'] != '':
        for i in range(3):
            board_buttons[i][i].config(bg='lightgreen')
        return True
    if board_buttons[0][2]['text'] == board_buttons[1][1]['text'] == board_buttons[2][0]['text'] != '':
        for i in range(3):
            board_buttons[i][2-i].config(bg='lightgreen')
        return True
    return False

def reset_game():
    global current_player
    global turn_counter
    global ai_is_next
    pvp_button.config(state='normal')
    pvc_button.config(state='normal')
    easy_button.config(state='normal')
    medium_button.config(state='normal')
    hard_button.config(state='normal')
    current_player = 'X'
    ai_is_next = True
    turn_counter = 0
    turn_label.config(text=f"{current_player}'s turn")
    for r in range(3):
        for c in range(3):
            board_buttons[r][c].config(text='', state='normal', bg='grey90')

# Game mode selection functions
def pvc():
    global ai_is_on
    easy_button.config(state='normal')
    medium_button.config(state='normal')
    hard_button.config(state='normal')
    ai_is_on = True

def pvp():
    global ai_is_on
    easy_button.config(state='disabled')
    medium_button.config(state='disabled')
    hard_button.config(state='disabled')
    ai_is_on = False

# GUI
window = tk.Tk()
window.title("Tic Tac Toe")

# Top controls in their own frame so sizing doesn't affect the board
top_frame = tk.Frame(window)
top_frame.grid(row=0, column=0, pady=6)

pvp_button = tk.Button(top_frame, text="Multiplayer", width=12, height=2, font=("Ariel", 18), command=pvp)
pvp_button.grid(column=0, row=0, padx=5)

pvc_button = tk.Button(top_frame, text="Computer", width=12, height=2, font=("Ariel", 18), command=pvc)
pvc_button.grid(column=1, row=0, padx=5)

game_play_frame = tk.Frame(window)
game_play_frame.grid(row=1, column=0, pady=6)

difficulty_label = tk.Label(game_play_frame, text="AI Difficulty:", font=("Ariel", 18))
difficulty_label.grid(column=1, row=0, padx=5)

easy_button = tk.Button(game_play_frame, text="Easy", width=8, height=2, font=("Ariel", 18), command=lambda: set_difficulty('Easy'))
easy_button.grid(column=0, row=1, padx=5)

medium_button = tk.Button(game_play_frame, text="Medium", width=8, height=2, font=("Ariel", 18), command=lambda: set_difficulty('Medium'))
medium_button.grid(column=1, row=1, padx=5)

hard_button = tk.Button(game_play_frame, text="Hard", width=8, height=2, font=("Ariel", 18), command=lambda: set_difficulty('Hard'))
hard_button.grid(column=2, row=1, padx=5)

turn_label = tk.Label(game_play_frame, text="X's turn", width=15, height=2, font=("Ariel", 18))
turn_label.grid(column=0, row=2, columnspan=3, pady=6)

# Board frame isolates the 3x3 grid
board_frame = tk.Frame(window)
board_frame.grid(row=2, column=0, padx=10, pady=8)

btn_props = dict(width=5, height=2, font=("Ariel", 18, "bold"), bg='grey90')

# Create a 3x3 list of board buttons and populate with a nested loop
board_buttons = [[None for _ in range(3)] for _ in range(3)]
for r in range(3):
    for c in range(3):
        # Use a lambda with default args to bind current r/c to the callback
        btn = tk.Button(board_frame, text='', **btn_props, command=lambda r=r, c=c: player_turn(r, c, board_buttons))
        btn.grid(row=r, column=c, padx=2, pady=2)
        board_buttons[r][c] = btn

bottom_frame = tk.Frame(window)
bottom_frame.grid(row=3, column=0, pady=6)

reset_button = tk.Button(bottom_frame, text="Reset Game", width=12, height=2, font=("Ariel", 18), command=reset_game)
reset_button.grid(column=0, row=0, padx=5)

window.mainloop()
