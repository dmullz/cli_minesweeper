import random

class Square:
	def __init__(self):
		self.guessed = False
		self.mine = False
		self.marked = False
		self.nearby = 0
	
	def set_guessed(self):
		self.guessed = True
	
	def set_marked(self):
		self.marked = not self.marked
		
	def set_mine(self):
		self.mine = True
	
	def set_nearby(self,num):
		self.nearby = num


class Minesweeper:
	def __init__(self,size,num_mines):
		self.size = size
		self.num_mines = num_mines
		self.create_board()
		self.started = False
	
	def create_board(self):
		self.board = [[Square() for col in range(self.size)] for row in range(self.size)]
	
	def check_win(self):
		for x in range(self.size):
			for y in range(self.size):
				if not self.board[x][y].mine and not self.board[x][y].guessed:
					return False
		return True
	
	def gen_nearby(self,x,y):
		if x-1 in range(self.size):
			yield (x-1,y)
		if x+1 in range(self.size):
			yield (x+1,y)
		if y-1 in range(self.size):
			yield (x,y-1)
		if y+1 in range(self.size):
			yield (x,y+1)
		if x-1 in range(self.size) and y-1 in range(self.size):
			yield (x-1,y-1)
		if x-1 in range(self.size) and y+1 in range(self.size):
			yield (x-1,y+1)
		if x+1 in range(self.size) and y-1 in range(self.size):
			yield (x+1,y-1)
		if x+1 in range(self.size) and y+1 in range(self.size):
			yield (x+1,y+1)
				
	def initialize_board(self,i,j):
		# Create set of mines
		mines = set()
		# Do not allow first box or any nearby clicked to be a mine
		mines.add((i,j))
		nearby_sqs = self.gen_nearby(i,j)
		for coords in nearby_sqs:
			mines.add((coords[0],coords[1]))
		# Populate mines and board with random mine placements
		for _ in range(self.num_mines):
			new_mine = (random.randint(0,self.size-1),random.randint(0,self.size-1))
			while new_mine in mines:
				new_mine = (random.randint(0,self.size-1),random.randint(0,self.size-1))
			mines.add(new_mine)
			self.board[new_mine[0]][new_mine[1]].set_mine()
		
		# Calculate nearby value for each square
		for x in range(self.size):
			for y in range(self.size):
				if self.board[x][y].mine == False:
					nearby = 0
					nearby_sqs = self.gen_nearby(x,y)
					for coords in nearby_sqs:
						if self.board[coords[0]][coords[1]].mine:
							nearby += 1
					self.board[x][y].set_nearby(nearby)
					
		# Print Revealed Board
		print("\n")
		for x in range(self.size):
			row = ""
			for y in range(self.size):
				if self.board[x][y].mine:
					row += 'X'
				else:
					row += str(self.board[x][y].nearby)
			print(row)
			
	def mark_square(self,x,y):
		if not self.board[x][y].marked:
			self.board[x][y].set_marked()
		
	def unmark_square(self,x,y):
		if self.board[x][y].marked:
			self.board[x][y].set_marked()
			
			
	def guess_square(self,x,y):
		if self.board[x][y].guessed:
			return "guessed"
		if self.board[x][y].marked:
			return "marked"
		if self.board[x][y].mine:
			return "mine"
		self.board[x][y].set_guessed()
		if not self.started:
			self.initialize_board(x,y)
			self.started = True	
		if self.board[x][y].nearby == 0:
			# Automatically guess all nearby squares
			nearby_sqs = self.gen_nearby(x,y)
			for coords in nearby_sqs:
				self.guess_square(coords[0],coords[1])
		if self.check_win():
			return "win"
		return "guessed"
	
	def display_board(self):
		row = "  "
		for x in range(self.size):
			row += chr(65+x)+" "
		print(row)
			
		for x in range(self.size):
			row = str(x+1)+" "
			for y in range(self.size):
				if self.board[x][y].guessed:
					if self.board[x][y].mine:
						row += 'X '
					else:
						row += str(self.board[x][y].nearby) +" "
				else:
					if self.board[x][y].marked:
						row += "M "
					else:
						row += "# "
			print(row)
		