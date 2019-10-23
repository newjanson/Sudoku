
import pygame as pg
import time as t

import random as r # Just used to remove numbers from board

class Sudoku_GUI:
	"""
	The Main GUI Application for Sudoku. 

	Runs the game based on user input.
	"""

	def __init__(self, dimensions) -> None:
		"""
		params:
		Initialize the sudoku game.
		Calcualte and store positioning and spacing values for UI.
		"""

		pg.init()  

		# Used to control the speed of game loop
		# Acts as a buffer for user input
		self.BUFFER_DELAY = (1/20) # 20 FPS

		# Color Palette
		self.BACKGROUND_COLOR = (0, 0, 0)
		self.MAJOR_LINE_COLOR = (200, 200, 200)
		self.MINOR_LINE_COLOR = (150, 150, 150)
		self.SELECTED_BOX_COLOR = (70, 70, 255)
		self.BUTTON_COLOR = (30, 30, 80)
		self.TEXT_COLOR = (250, 250, 250)

		# Line Widths
		self.MAJOR_LINE_WIDTH = 6
		self.MINOR_LINE_WIDTH = 1

		# Fonts
		self.NUMBER_FONT = pg.font.SysFont('Consolas', 50)
		self.BUTTON_FONT = pg.font.SysFont('Consolas', 30)

		# The dimensions of the window (window is dimensions x dimensions)
		self.dimensions = dimensions

		# The dimensions of the buttons
		self.button_width = self.dimensions / 3
		self.button_height = 70
		self.button_padding = 10
		self.button_y_pos = self.dimensions + self.button_padding
		self.pause_x_pos = self.button_padding
		self.clear_x_pos = self.button_width + self.button_padding
		self.main_menu_x_pos = 2*self.button_width + self.button_padding
		
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

	def _render_sudoku_board(self, render_screen) -> None:
		"""
		Render the sudoku board on the screen by
		drawing the grid lines, the numbers and the
		buttons. 
		"""

		# Reset Screen
		render_screen.fill(self.BACKGROUND_COLOR)

		# Draw Grid Lines and Selected Box
		self._render_grid(render_screen)

		# Draw Numbers
		self._render_numbers(render_screen)

		# Draw Buttons
		self._render_buttons(render_screen)

	def _render_grid(self, render_screen) -> None:
		"""
		Draw thin lines to represnet smaller box.
		Draw thick lines to represent the nonets.
		Draw square to represent selected box. 
		"""

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

	def _render_numbers(self, render_screen) -> None:
		"""
		Draw the numbers and place them inside the box.
		"""

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

	def _render_buttons(self, render_screen) -> None:
		"""
		Draw the three button rectangles and place the
		button text inside the rectangles.
		"""
	
		# Pause Button
		pg.draw.rect(render_screen, self.BUTTON_COLOR, 
		(self.pause_x_pos, self.button_y_pos, \
		self.button_width - 2*self.button_padding, self.button_height - 2*self.button_padding))
		
		px = self.pause_x_pos + ((self.button_width - 2*self.button_padding) // 2)
		py = self.button_y_pos + ((self.button_height - 2*self.button_padding) // 2)

		text_surface = self.BUTTON_FONT.render("PAUSE", True, self.TEXT_COLOR)
		render_screen.blit(text_surface, text_surface.get_rect(center=(px, py)))

		# Clear Button
		pg.draw.rect(render_screen, self.BUTTON_COLOR, 
		(self.clear_x_pos, self.button_y_pos, \
		self.button_width - 2*self.button_padding, self.button_height - 2*self.button_padding))

		px = self.clear_x_pos + ((self.button_width - 2*self.button_padding) // 2)
		py = self.button_y_pos + ((self.button_height - 2*self.button_padding) // 2)

		text_surface = self.BUTTON_FONT.render("CLEAR", True, self.TEXT_COLOR)
		render_screen.blit(text_surface, text_surface.get_rect(center=(px, py)))

		# Main Menu Button
		pg.draw.rect(render_screen, self.BUTTON_COLOR, 
		(self.main_menu_x_pos, self.button_y_pos, \
		self.button_width - 2*self.button_padding, self.button_height - 2*self.button_padding))

		px = self.main_menu_x_pos + ((self.button_width - 2*self.button_padding) // 2)
		py = self.button_y_pos + ((self.button_height - 2*self.button_padding) // 2)

		text_surface = self.BUTTON_FONT.render("MAIN MENU", True, self.TEXT_COLOR)
		render_screen.blit(text_surface, text_surface.get_rect(center=(px, py)))

	def _update_current_selected_box_pos(self, user_input, is_mouse) -> None:
		"""
		Parse user input and update position of the current selected box
		"""
		
		# user_input can be a keyboard direction
		# or it can be a mouse position

		if not is_mouse:
			dr = user_input[0]
			dc = user_input[1]

			# Update current selected box only if direction is valid
			self.curr_selected_row += dr * int(0 <= self.curr_selected_row + dr <= 8)
			self.curr_selected_col += dc * int(0 <= self.curr_selected_col + dc <= 8)
		
		else:
			mx = user_input[0]
			my = user_input[1]

			# Convert mouse position to array position
			row = int(my // self.minor_box_y_interval)
			col = int(mx // self.minor_box_x_interval)

			if 0 <= row <= 8 and 0 <= col <= 8:
				self.curr_selected_row = row
				self.curr_selected_col = col


	def _get_player_input(self) -> tuple:
		"""
		Get the user's directional input, number key input, and
		mouse position input and return it as a tuple
		"""

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

		# Check Mouse Input
		mouse_pos = self._check_player_mouse()

		return move_direction, placed_num, mouse_pos

	def _check_player_mouse(self) -> tuple:
		"""
		Return mouse position as a tuple if left click pressed.
		Return None if left click not pressed.
		"""

		mouse_button_state = pg.mouse.get_pressed()
		
		# Left Click
		if mouse_button_state[0]:
			
			# Mouse xy position
			mx, my = pg.mouse.get_pos()

			# Check if mouse is in Pause Button Rectangle
			if self.pause_x_pos <= mx <= self.pause_x_pos + (self.button_width - 2*self.button_padding):
				if self.button_y_pos <= my <= self.button_y_pos  + (self.button_height - 2*self.button_padding):
					# Pause Button pressed
					self._on_pause_click()

			# Check if mouse is in Clear Button Rectangle
			elif self.clear_x_pos <= mx <= self.clear_x_pos + (self.button_width - 2*self.button_padding):
				if self.button_y_pos  <= my <= self.button_y_pos  + (self.button_height - 2*self.button_padding):
					# Clear Button pressed
					self._on_clear_click()

			# Check if mouse is in Main Menu Button Rectangle
			elif self.main_menu_x_pos <= mx <= self.main_menu_x_pos + (self.button_width - 2*self.button_padding):
				if self.button_y_pos  <= my <= self.button_y_pos  + (self.button_height - 2*self.button_padding):
					# Main Menu Button pressed
					self._on_main_menu_click()

			return (mx, my)

	def _on_pause_click(self):
		"""
		Will be implemented by Greg and Aditya
		"""
		# TODO Implement this method
		print("PAUSE BUTTON PRESSED")

	def _on_clear_click(self):
		"""
		Will be implemented by Greg and Aditya
		"""
		# TODO Implement this method
		print("CLEAR BUTTON PRESSED")

	def _on_main_menu_click(self):
		"""
		Will be implemented by Greg and Aditya
		"""
		# TODO Implement this method
		print("MAIN MENU BUTTON PRESSED")

	def run_game(self) -> None:
		"""
		Initialize the game and run the main game loop
		"""

		# Initialize PyGame Screen      
		game_screen = pg.display.set_mode((self.dimensions, self.dimensions + self.button_height))    
		pg.display.set_caption('PyDoku Inc.')

		game_over = False

		self._render_sudoku_board(game_screen)		

		while not game_over:

			# Poll user input
			event = pg.event.poll()
			# User closed the window
			if event.type == pg.QUIT: 
				return
	
			# Input for moving the selected box
			user_input, placed_num, mouse_pos = self._get_player_input()
			
			board_changed = False

			# If user inputs a number other than 0
			if placed_num:
				self.board[self.curr_selected_row][self.curr_selected_col] = placed_num
				board_changed = True

			# If user moves the selected box in a direction other than (0, 0)
			if any(user_input):
				self._update_current_selected_box_pos(user_input, False)
				board_changed = True

			# If the user clicked on the screen
			if mouse_pos is not None:
				self._update_current_selected_box_pos(mouse_pos, True)
				board_changed = True
			
			# If the state of the board has changed
			if board_changed:
				self._render_sudoku_board(game_screen)
	
			pg.display.update()

			# Delay the game loop to act as a buffer
			t.sleep(self.BUFFER_DELAY)


if __name__ == "__main__":
	
	game = Sudoku_GUI(600)
	game.run_game()