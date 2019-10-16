
import pygame as pg


class Sudoku_GUI:

	def __init__(self, dimensions):

		# Used to control the speed of game loop
		# Acts as a buffer for user input
		self.BUFFER_DELAY = 0.05 # 50 ms

		# Color Palette
		self.MAJOR_LINE_COLOR = (250, 250, 250)
		self.MINOR_LINE_COLOR = (150, 150, 150)
		self.TEXT_COLOR = (200, 200, 200)
		self.SELECTED_BOX_COLOR = (180, 180, 255)

		# Line Widths
		self.MAJOR_LINE_WIDTH = 6
		self.MINOR_LINE_WIDTH = 1

		# The dimensions of the window (window is dimensions x dimensions)
		self.dimensions = dimensions

		# The interval of major box in each direction
		self.major_box_x_interval = self.dimensions // 3
		self.major_box_y_interval = self.dimensions // 3

		# The interval of minor box inside the major box in each direction
		self.minor_box_x_interval = self.dimensions // 9
		self.minor_box_y_interval = self.dimensions // 9

		# Uncomment when Yaman is done with Sudoku
		# self.sudoku = Sudoku(<params>)

		# Represents the current selected box
		self.curr_selected_row = 0
		self.curr_selected_col = 0


	def _draw_grid_lines(self, render_screen):

		# Draw Outline Border
		pg.draw.rect(render_screen, self.MAJOR_LINE_COLOR, (0, 0, self.dimensions, self.dimensions), 5)

		# Draw Minor Lines
		for i in range(3):
			for j in range(1, 3):
				# Vertical Lines
				pg.draw.line(render_screen, self.MINOR_LINE_COLOR, ((self.major_box_x_interval*i) + (self.minor_box_x_interval*j), 0), \
				((self.major_box_x_interval*i) + (self.minor_box_x_interval*j), self.dimensions), self.MINOR_LINE_WIDTH)

				# Horizontal Lines
				pg.draw.line(render_screen, self.MINOR_LINE_COLOR, (0, (self.major_box_y_interval*i) + (self.minor_box_y_interval*j)), \
				(self.dimensions, (self.major_box_y_interval*i) + (self.minor_box_y_interval*j)), self.MINOR_LINE_WIDTH)

		# Draw Major lines
		for i in range(1, 3):
			# Vertical Lines
			pg.draw.line(render_screen, self.MAJOR_LINE_COLOR, (self.major_box_x_interval*i, 0), \
			(self.major_box_x_interval*i, self.dimensions), self.MAJOR_LINE_WIDTH)

			# Horizontal Lines
			pg.draw.line(render_screen, self.MAJOR_LINE_COLOR, (0, self.major_box_y_interval*i), \
			(self.dimensions, self.major_box_y_interval*i), self.MAJOR_LINE_WIDTH)



	def _draw_board(self, render_screen):
		raise NotImplementedError

	def _update_current_selected_box(self, input_direction):
		raise NotImplementedError

	def run_game(self):

		# Initialize PyGame
		pg.init()        
		game_screen = pg.display.set_mode((self.dimensions, self.dimensions))    
		pg.display.set_caption('PyDoku Inc.')
		font = pg.font.SysFont('Courier New', 20)

		game_over = False

		self._draw_grid_lines(game_screen)		

		while not game_over:

			# Poll user input
			event = pg.event.poll()

			# User closed the window
			if event.type == pg.QUIT: 
				return

			# User keyboard input
			keys = pg.key.get_pressed()

			# The direction the selected box is moving
			input_direction = [0, 0] 
			if keys[pg.K_UP]: # Up Direction
				input_direction = [-1, 0]
			elif keys[pg.K_DOWN]: # Down Direction
				input_direction = [1, 0]
			elif keys[pg.K_LEFT]: # Left Direction
				input_direction = [0, -1]
			elif keys[pg.K_RIGHT]: # Right Direction
				input_direction = [0, 1]

			# self._update_current_selected_box(input_direction);

			pg.display.update()

if __name__ == "__main__":
	
	game = Sudoku_GUI(700)
	game.run_game()