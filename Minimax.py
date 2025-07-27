
"""
Author => R.Dinesh
founder and CEO of auravia

"""


import numpy as np

win_patterns = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

def print_grid(grid):
    print("\nCurrent Board:")
    for i in range(0, 9, 3):
        print(grid[i], grid[i+1], grid[i+2])
    print()

def check_winner(grid, ai, human):
    ai_moves = [i for i, x in enumerate(grid) if x == ai]
    human_moves = [i for i, x in enumerate(grid) if x == human]
    for pattern in win_patterns:
        if all(p in ai_moves for p in pattern):
            return 'AI'
        if all(p in human_moves for p in pattern):
            return 'Human'
    if '.' not in grid:
        return 'Draw'
    return None

def minimax(grid, is_ai_turn, ai, human):
    result = check_winner(grid, ai, human)
    if result == 'AI':
        return 10
    elif result == 'Human':
        return -10
    elif result == 'Draw':
        return 0

    available = [i for i in range(9) if grid[i] == '.']
    if is_ai_turn:
        best_score = -float('inf')
        for i in available:
            grid[i] = ai
            score = minimax(grid, False, ai, human)
            grid[i] = '.'
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in available:
            grid[i] = human
            score = minimax(grid, True, ai, human)
            grid[i] = '.'
            best_score = min(best_score, score)
        return best_score

def ai_move(grid, ai, human):
    best_score = -float('inf')
    best_move = -1
    for i in range(9):
        if grid[i] == '.':
            grid[i] = ai
            score = minimax(grid, False, ai, human)
            grid[i] = '.'
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

# Main Game
def play_game():
    grid = ['.'] * 9
    ai = 'x'
    human = 'o'

    print("Tic Tac Toe! You are 'o', AI is 'x'")
    print("Positions are from 0 to 8 like this:")
    print("0 1 2\n3 4 5\n6 7 8")
    
    print_grid(grid)

    while True:
        # Human move
        while True:
            try:
                move = int(input("Enter your move (0–8): "))
                if grid[move] == '.':
                    grid[move] = human
                    break
                else:
                    print("Position already taken.")
            except:
                print("Invalid input. Enter a number from 0 to 8.")

        print_grid(grid)
        winner = check_winner(grid, ai, human)
        if winner:
            print("Winner:", winner)
            break

        # AI move
        print("AI is thinking...")
        move = ai_move(grid, ai, human)
        grid[move] = ai
        print(f"AI moved to {move}")
        print_grid(grid)

        winner = check_winner(grid, ai, human)
        if winner:
            print("Winner:", winner)
            break

# Start the game
play_game()
