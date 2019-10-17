
import pygame as pg
import time as t

import random as r # Just used to remove numbers from board

class Sudoku_GUI:

	def __init__(self, dimensions):

		pg.init()  

		# Used to control the speed of game loop
		# Acts as a buffer for user input
		self.BUFFER_DELAY = 0.1 # 100 ms

		# Color Palette
		self.MAJOR_LINE_COLOR = (250, 250, 250)
		self.MINOR_LINE_COLOR = (150, 150, 150)
		self.TEXT_COLOR = (250, 250, 250)
		self.SELECTED_BOX_COLOR = (80, 80, 255)
		self.BACKGROUND_COLOR = (0, 0, 0)

		# Line Widths
		self.MAJOR_LINE_WIDTH = 6
		self.MINOR_LINE_WIDTH = 1

		# Fonts
		self.NUMBER_FONT = pg.font.SysFont('Consolas', 50)

		# The dimensions of the window (window is dimensions x dimensions)
		self.dimensions = dimensions

		# The interval of major box in each direction
		self.major_box_x_interval = self.dimensions / 3
		self.major_box_y_interval = self.dimensions / 3

		# The interval of minor box inside the major box in each direction
		self.minor_box_x_interval = self.dimensions / 9
		self.minor_box_y_interval = self.dimensions / 9

		# Uncomment when Yaman is done with Sudoku
		# self.sudoku = Sudoku(<params>)

		# Using temporary board for numbers
		# Below code just generates a random board (not Sudoku based board)
		# Delete this once Yaman's class is integrated
		self.board = [[i for i in range(1, 10)] for j in range(1, 10)]
		for i in range(len(self.board)):
			for j in range(len(self.board[i])):
				if r.random() <= 0.3: # 30% chance of removing
					self.board[i][j] = 0


		# Represents the current selected box
		self.curr_selected_row = 0
		self.curr_selected_col = 0


	def _render_grid(self, render_screen):

		render_screen.fill(self.BACKGROUND_COLOR)

		# Draw Minor Lines
		for i in range(3):
			for j in range(1, 3):
				# Vertical Lines
				pg.draw.line(render_screen, self.MINOR_LINE_COLOR, ((self.major_box_x_interval*i) + (self.minor_box_x_interval*j), 0), \
				((self.major_box_x_interval*i) + (self.minor_box_x_interval*j), self.dimensions), self.MINOR_LINE_WIDTH)

				# Horizontal Lines
				pg.draw.line(render_screen, self.MINOR_LINE_COLOR, (0, (self.major_box_y_interval*i) + (self.minor_box_y_interval*j)), \
				(self.dimensions, (self.major_box_y_interval*i) + (self.minor_box_y_interval*j)), self.MINOR_LINE_WIDTH)

		# Draw Major Lines
		for i in range(1, 3):
			# Vertical Lines
			pg.draw.line(render_screen, self.MAJOR_LINE_COLOR, (self.major_box_x_interval*i, 0), \
			(self.major_box_x_interval*i, self.dimensions), self.MAJOR_LINE_WIDTH)

			# Horizontal Lines
			pg.draw.line(render_screen, self.MAJOR_LINE_COLOR, (0, self.major_box_y_interval*i), \
			(self.dimensions, self.major_box_y_interval*i), self.MAJOR_LINE_WIDTH)

		# Draw Outline Border of screen
		pg.draw.rect(render_screen, self.MAJOR_LINE_COLOR, (0, 0, self.dimensions, self.dimensions), 5)

		# Draw Selected Box
		pg.draw.rect(render_screen, self.SELECTED_BOX_COLOR,
		(self.minor_box_x_interval * self.curr_selected_col, self.minor_box_y_interval * self.curr_selected_row, \
		self.minor_box_x_interval, self.minor_box_y_interval), self.MAJOR_LINE_WIDTH)

		# Draw numbers
		self._render_numbers(render_screen)

	def _render_numbers(self, render_screen):
	
		for row in range(len(self.board)):
			for col in range(len(self.board[row])):

				val = self.board[row][col]
				if val:
					value_string = str(val)
					text_surface = self.NUMBER_FONT.render(value_string, True, self.TEXT_COLOR)
					
					# Text position
					px = (self.minor_box_x_interval * col) + (self.minor_box_x_interval / 2)
					py = (self.minor_box_y_interval * row) + (self.minor_box_y_interval / 2)
					
					# Center the text
					text_rect = text_surface.get_rect(center=(px, py))

					render_screen.blit(text_surface, text_rect)


	def _update_current_selected_box(self, input_direction):
		
		dr = input_direction[0]
		dc = input_direction[1]

		# Update current selected box only if direction is valid
		self.curr_selected_row += dr * int(0 <= self.curr_selected_row + dr <= 8)
		self.curr_selected_col += dc * int(0 <= self.curr_selected_col + dc <= 8)

	def _get_player_input(self):

		# User keyboard input
		keys = pg.key.get_pressed()

		move_direction = [0, 0]
		# The direction the selected box is moving
		if keys[pg.K_UP] or keys[pg.K_w]: # Up Direction
			move_direction = [-1, 0]
		elif keys[pg.K_DOWN] or keys[pg.K_s]: # Down Direction
			move_direction = [1, 0]
		elif keys[pg.K_LEFT] or keys[pg.K_a]: # Left Direction
			move_direction = [0, -1]
		elif keys[pg.K_RIGHT] or keys[pg.K_d]: # Right Direction
			move_direction = [0, 1]

		placed_num = 0
		# The number input from user
		# I can't think of a better way lmao
		if keys[pg.K_1]:
			placed_num = 1
		elif keys[pg.K_2]:
			placed_num = 2
		elif keys[pg.K_3]:
			placed_num = 3
		elif keys[pg.K_4]:
			placed_num = 4
		elif keys[pg.K_5]:
			placed_num = 5
		elif keys[pg.K_6]:
			placed_num = 6
		elif keys[pg.K_7]:
			placed_num = 7
		elif keys[pg.K_8]:
			placed_num = 8
		elif keys[pg.K_9]:
			placed_num = 9

		return move_direction, placed_num

		raise NotImplementedError

	def run_game(self):

		# Initialize PyGame      
		game_screen = pg.display.set_mode((self.dimensions, self.dimensions))    
		pg.display.set_caption('PyDoku Inc.')


		game_over = False

		self._render_grid(game_screen)		

		while not game_over:

			# Poll user input
			event = pg.event.poll()
			# User closed the window
			if event.type == pg.QUIT: 
				return
	
			# Input for moving the selected box
			input_direction, placed_num = self._get_player_input()
			
			board_changed = False

			if placed_num:
				self.board[self.curr_selected_row][self.curr_selected_col] = placed_num
				board_changed = True

			if any(input_direction):
				self._update_current_selected_box(input_direction)
				board_changed = True
			
			if board_changed:
				self._render_grid(game_screen)
	

			pg.display.update()
			t.sleep(self.BUFFER_DELAY)


if __name__ == "__main__":
	
	game = Sudoku_GUI(700)
	game.run_game()