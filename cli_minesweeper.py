import minesweeper
import re
from os import system, name 
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def print_help():
	clear()
	print("To play, mark mines with 'M' and guess open squares with 'G'.")
	print("Use the coordinate system to select the correct square, starting with the letter first.")
	print("Example: GA1 guesses the top left corner square.")
	print("Type 'exit' to exit the game.")
	_ = input("Press any key to continue.")

def play_game():
	board = minesweeper.Minesweeper(9,10)
	
	while True:
		clear()
		print("\nWelcome to minesweeper.\n")
		board.display_board()
		guess = input("\nMake an action: ")
		if not re.match(r'^[GMU][A-I][1-9]', guess):
			if guess == "exit":
				break
			print_help()
			continue
		if guess[0] == 'G':
			result = board.guess_square(int(guess[2])-1,ord(guess[1])-65)
			if result == "mine":
				clear()
				print("\nWelcome to minesweeper.\n")
				board.display_board()
				print("\nYOU LOSE\n")
				play_again = input("Play again? (Y/N)")
				if play_again == "Y":
					board = minesweeper.Minesweeper(9,10)
					continue
				break
			if result == "marked":
				print("\nYou cannot guess a square that you have marked as a mine.\n")
				_ = input("Hit any key to continue.")
				continue
			if result == "win":
				clear()
				print("\nWelcome to minesweeper.\n")
				board.display_board()
				print("\nYOU WIN\n")
				play_again = input("Play again? (Y/N)")
				if play_again == "Y":
					board = minesweeper.Minesweeper(9,10)
					continue
				break
		if guess[0] == 'M':
			board.mark_square(int(guess[2])-1,ord(guess[1])-65)
			clear()
			board.display_board()
		if guess[0] == 'U':
			board.unmark_square(int(guess[2])-1,ord(guess[1])-65)
			clear()
			board.display_board()
			
			
play_game()