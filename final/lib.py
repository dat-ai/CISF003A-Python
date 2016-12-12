import pygame, itertools


# Color variables. These might will be use when constructing a new objects in pygame(lines, circles)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLACK = (84, 84, 84)                # X mark
DARK_GRAY = (20, 189, 172)          # Background
LIGHT_YELLOW = (242, 235, 211)      # O Mark
LIGHT_GREEN = (13, 161, 146)        # GridLine

# SOUND Global variables
M_START = "./sound/start.wav"
M_P1 = "./sound/player1.wav"
M_P2 = "./sound/player2.wav"
M_WINNER = "./sound/winner.wav"
M_DRAW = "./sound/draw.wav"


class Box(object):
    """
    Box where the x's and o's are drawn

    :param state: global variables [default = 0, if box is marked then state = 1]
    :param size: size of the box
    :param line_width: width of the X mark
    :param rect: pygame rectangle is drawn on this box
    :param board: the board this box uses to drawn
    """
    state = 0

    def __init__(self, x, y, size, board):
        """
        Initialize a box

        :param x: x-axis value
        :param y: y-axis value
        :param size: size of this box
        :param board: the board it will use to draw
        """
        self.size = size
        self.line_width = int(self.size / 6) if self.size > 40 else 1
        self.radius = (self.size / 2) - (self.size / 8)
        self.rect = pygame.Rect(x, y, size, size)
        self.board = board
    
    def mark_x(self):
        """
        Mark X on the screen when player clicks on the screen

        :return: draw X mark on the box that player clicks
        """
        s = self.line_width
        r = self.radius
        pygame.draw.line(self.board.surface, BLACK, (self.rect.centerx - r, self.rect.centery - r), (self.rect.centerx + r, self.rect.centery + r), s)
        pygame.draw.line(self.board.surface, BLACK, (self.rect.centerx - r, self.rect.centery + r), (self.rect.centerx + r, self.rect.centery - r), s)
    
    def mark_o(self):
        """
        Mark O on the screen when player clicks on the screen

        :return: draw an O mark on the box that player clicks
        """
        s = self.line_width
        r = self.radius
        pygame.draw.circle(self.board.surface, LIGHT_YELLOW, (int(self.rect.centerx), int(self.rect.centery)), int(r), int(s))


class Board(object):
    """
    TicTacToe Board

    :param grid_size: number of grids in the Board (Default = 3)
    :param box_size:  number of boxes in the Board (Default = 200)
    :param border:    the border of the board to determine where to start drawing
    :param line_width: the width of lines that separate each box
    :param surface_size: size of the window
    :param surface:   Game window
    :param game_over: state if game is over
    :param result:    save result of player 1 and player [default = 0,0]. update after every game
    """
    turn = 1
    
    def __init__(self, grid_size=3, box_size=200, border=20, line_width=5):
        self.grid_size = grid_size
        self.box_size = box_size
        self.border = border
        self.line_width = line_width
        self.surface_size = (self.grid_size * self.box_size) + (self.border * 2) + (self.line_width * (self.grid_size - 1))
        self.surface = pygame.display.set_mode((self.surface_size, self.surface_size), 0, 32)
        self.game_over = False
        self.result = [0, 0]
        pygame.display.set_caption('Tic Tac Toe - Final Project')
        self.add_sound(M_START)
        self.display_start_screen()
        self.setup()
        
    def setup(self):
        """
        Create a window on the screen.

        :return: nothing
        """
        self.surface.fill(DARK_GRAY)
        self.draw_lines()
        self.initialize_boxes()
        self.add_text_to_screen("Turn: Player %s" % self.turn, BLACK, "small", int(self.surface_size/2.2), DARK_GRAY)
        self.calculate_winners()

    def draw_lines(self):
        """
        Draw lines on the Board.

        :return: display grid-lines on the board
        """
        for i in range(1, self.grid_size):
            start_position = ((self.box_size * i) + (self.line_width * (i - 1))) + self.border
            width = self.surface.get_width() - (2 * self.border)
            pygame.draw.rect(self.surface, LIGHT_GREEN, (start_position, self.border, self.line_width, width))
            pygame.draw.rect(self.surface, LIGHT_GREEN, (self.border, start_position, width, self.line_width))
    
    def initialize_boxes(self):
        """
        Create boxes for the TicTacToe Board

        :return: set up all the boxes on the screen window
        """
        self.boxes = []
        top_left_numbers = []
        for i in range(0, self.grid_size):
            num = ((i * self.box_size) + self.border + (i * self.line_width))
            top_left_numbers.append(num)
        box_coordinates = list(itertools.product(top_left_numbers, repeat=2))
        for x, y in box_coordinates:
            self.boxes.append(Box(x, y, self.box_size, self))
    
    def get_box_at_pixel(self, x, y):
        """
        Get which box play has clicked

        :param x: x-axis value on the window
        :param y: y-axis value on the window

        :return: box where player clicks. None if box is not found
        """
        for index, box in enumerate(self.boxes):
            if box.rect.collidepoint(x, y):
                return box
        return None
    
    def process_click(self, x, y):
        """
        Process where player clicks and feedback appropriate actions if player clicks in BOX area:

        :param x: x-axis value
        :param y: y-axis value
        :return:
        """
        box = self.get_box_at_pixel(x, y)
        if box is not None and not self.game_over:
            self.play_turn(box)
            self.add_text_to_screen("Turn: Player %s" % self.turn, BLACK, "small", int(self.surface_size / 2.2), DARK_GRAY)
            self.check_game_over()

    def play_turn(self, box):
        """
        Determine turn of players and draw line/circle
        X = 1
        O = 2

        :param box: a box user has selected
        :return:
        """

        if box.state != 0:
            return
        if self.turn == 1:
            self.add_sound(M_P1)
            box.mark_x()
            box.state = 1
            self.turn = 2
        elif self.turn == 2:
            self.add_sound(M_P2)
            box.mark_o()
            box.state = 2
            self.turn = 1

        return
    
    def calculate_winners(self):
        """
        Count all selected boxes by a player is enough to be a winner

        :return: nothing
        """
        self.winning_combinations = []
        indices = [x for x in range(0, self.grid_size * self.grid_size)]
        
        # Vertical combinations
        self.winning_combinations += ([tuple(indices[i:i+self.grid_size]) for i in range(0, len(indices), self.grid_size)])
        
        # Horizontal combinations
        self.winning_combinations += [tuple([indices[x] for x in range(y, len(indices), self.grid_size)]) for y in range(0, self.grid_size)]
        
        # Diagonal combinations
        self.winning_combinations.append(tuple(x for x in range(0, len(indices), self.grid_size + 1)))
        self.winning_combinations.append(tuple(x for x in range(self.grid_size - 1, len(indices), self.grid_size - 1)))
    
    def check_for_winner(self):
        """
        Determine if the winner is found

        :return: winner
        """
        winner = 0
        for combination in self.winning_combinations:
            states = []
            for index in combination:
                states.append(self.boxes[index].state)
            if all(x == 1 for x in states):
                winner = 1
                self.result[0] += 1
            if all(x == 2 for x in states):
                winner = 2
                self.result[1] += 1
        return winner
    
    def check_game_over(self):
        """
        Determine if the game is over.

        :return: update self.game_over
        """
        winner = self.check_for_winner()
        if winner:
            self.game_over = True
        elif all(box.state in [1, 2] for box in self.boxes):
            self.game_over = True
        if self.game_over:
            self.display_game_over(winner)

    def display_start_screen(self):
        """
        Display an Instruction screen before players starting the game

        :return:
        """
        intro = True
        x = self.surface_size
        button_pos = (x/2 - x*0.16, x - x*0.2, 150, 100)
        while intro:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            # Create a blank white screen
            self.surface.fill(LIGHT_GREEN)
            self.add_text_to_screen("Welcome to TicTacToe Game", WHITE, "large", -self.surface_size*0.05, LIGHT_GREEN )
            self.add_text_to_screen("CIS F003A - Fall 2016", WHITE, "small", self.surface_size*0.05, LIGHT_GREEN)
            self.add_button(button_pos, DARK_GRAY, "Click me to continue", WHITE)
            if self.is_hover(button_pos):
                click = pygame.mouse.get_pressed()
                if click[0] == 1:
                    break
                self.add_button(button_pos, WHITE, "Click me to continue", BLACK)
            pygame.display.update()

    def display_game_over(self, winner):
        """
        Display the game result : winner is found or a draw game

        :param winner: the winner
        :return: dispaly winner and current scores
        """
        if winner:
            self.add_sound(M_WINNER)
            text = 'Player %s won!' % winner
        else:
            self.add_sound(M_DRAW)
            text = 'Draw Game!'

        # Display result
        self.surface.fill(DARK_GRAY)
        self.add_text_to_screen(text, BLACK, 60, 0, DARK_GRAY)
        # Restart or quit
        x = self.surface_size
        restart_button = (x / 2 - x * 0.40, x - x*0.2, 150, 100)
        quit_button = (x / 2 + x * 0.05, x - x*0.2, 150, 100)
        p_one = "Player 1: %s" % str(self.result[0])
        p_two = "Player 2: %s" % str(self.result[1])

        self.add_text_to_screen(p_one, LIGHT_GREEN, "small", -int(x/2.2), DARK_GRAY, -int(x*0.25))
        self.add_text_to_screen(p_two, LIGHT_GREEN, "small", -int(x/2.2), DARK_GRAY, int(x*0.25))
        end = True
        while end:
            self.add_button(restart_button, DARK_GRAY, "Restart", LIGHT_GREEN)
            self.add_button(quit_button, DARK_GRAY, "Quit", LIGHT_GREEN)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            # If user click restart button, break the loop
            if self.is_hover(restart_button):
                click = pygame.mouse.get_pressed()
                self.add_button(restart_button, DARK_GRAY, "Restart", WHITE)
                if click[0] == 1:
                    break
            # If user enter quit button, quit the program
            if self.is_hover(quit_button):
                click = pygame.mouse.get_pressed()
                self.add_button(quit_button, DARK_GRAY, "Quit", WHITE)
                if click[0] == 1:
                    pygame.quit()
                    quit()

            pygame.display.update()

        # Restart the game
        self.reset()

    def add_text_to_screen(self, message, color, size="small", yoffset=0, rect_color=(255, 255, 255), xoffset=0):
        """
        Display a message at the middle of the screen

        :param message: the message to the screen
        :param color:   color of the text
        :param size:    size of the size
        :param xoffset: offset to the middle horizontal position [default = 0]
        :param yoffset: offset to the middle vertical position [default = 0]
        :param rect_color: background color [default is white[
        :return:
        """
        text, rect = self.text_objects(message, color, size, rect_color)
        rect.center = (self.surface_size / 2 + xoffset, self.surface_size / 2 + yoffset)
        self.surface.blit(text, rect)

    def add_button(self, size, color, text, text_color):
        """
        Add a button to the screen

        :param size: array_like shape of the button.
        :param color: color for the button
        :param text: message of the text
        :param text_color: color of the text
        :return: a button the screen
        """
        text_surf, text_rect = self.text_objects(text, text_color, "small", color)
        text_rect.center = ((size[0] + size[2] / 2), (size[1] + size[3] / 2))
        self.surface.blit(text_surf, text_rect)

    def add_sound(self, filepath):
        """
        Add sound to the game
        :param filepath: path to the audio file
        :return:
        """
        new_sound = pygame.mixer.Sound(filepath)
        new_sound.play()

    def text_objects(self, text, color, size="small", rect_color=(255, 255, 255)):
        """
        Create a dynamic text object

        :param text: message
        :param color: RGB color
        :param size: size "small", "medium", "large" [default = small]
        :param rect_color: color of the rectangle boundary

        :return: text, text_surface

        """
        text_surf = None
        small_font = pygame.font.SysFont(None, int(self.surface_size / 15))
        medium_font = pygame.font.SysFont(None, int(self.surface_size / 13))
        large_font = pygame.font.SysFont(None, int(self.surface_size / 10))
        if size == "small":
            text_surf = small_font.render(text, True, color, rect_color)
        elif size == "medium":
            text_surf = medium_font.render(text, True, color, rect_color)
        elif size == "large":
            text_surf = large_font.render(text, True, color, rect_color)
        else:
            custom_font = pygame.font.SysFont(None, int(size))
            text_surf = custom_font.render(text, True, color, rect_color)

        return text_surf, text_surf.get_rect()

    def reset(self):
        """
        Reset for a new game

        :return:
        """
        self.game_over = False
        self.setup()

    def is_hover(self, pos):
        """
        Check if mouse hover a button

        :param pos: position of a button
        :return: true or false
        """
        cur = pygame.mouse.get_pos()
        if pos[0] + pos[2] > cur[0] > pos[0] and pos[1] + pos[3] > cur[1] > pos[1]:
            return True
        else:
            False

    def add_sound(self, path):
        """
        Add sound to the game
        :param self:
        :param path: path to audio file
        :return: play sound
        """
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()