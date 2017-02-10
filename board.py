#!/usr/bin/python
import random
import re

class board(object):
    def __update_cell_value(self, x, y):
        if(x >= 0 and x < self.row and y >= 0 and y < self.col and self.revealed[x][y] != -1):
            self.revealed[x][y] += 1

    def __update_cell(self, x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                self.__update_cell_value(x+i, y+j)


    def __init__(self, row = 16, col = 16, total = 51):
        self.board = []
        self.row = row
        self.col = col
        self.total = total

        # Initialize to 0s
        self.revealed = [[0 for x in range(col)] for y in range(row)]

        # Entire board is 'o's. As players click, the grid reveals.
        # 'o' - unrevealed, -1 - player 1, -2 - player 2, 0-8 - bombs around it
        self.game = [['o' for x in range(col)] for y in range(row)]
        self.player = 0
        # Player 1 - Blue, 2 - Red
        self.player_colors = ['B', 'R']

        numerator = total
        denominator = row * col

        # -1 = Bomb
        # 0-8 = Numbers in grid
        for x in range(0, row):
            self.board.append([])
            self.revealed.append([])
            for y in range(0, col):
                if( random.random() < (1.0 * numerator/denominator) ):
                    self.board[x].append('x')
                    self.revealed[x][y] = -1
                    self.__update_cell(x, y)
                    numerator -= 1
                else:
                    self.board[x].append('o')
                denominator -= 1

    def pretty_print(self, obj, format_spec):
        for row in range(0,self.row):
            my_str = ''
            for col in range(0,self.col):
                my_str += format_spec(obj[row][col])+' '
            print(my_str)

    def pretty_print_chars(self):
        self.pretty_print(self.board, lambda x: '%s' %x)

    def pretty_print_grid(self):
        self.pretty_print(self.revealed, lambda x: '%2d' %x)

    def set_color(self, player, color):
        if(player > 2 or player < 0):
            print('Player should be either 1 or 2')
        elif(re.search('^[a-zA-Z]$', color)):
            # Compiling the RE on the fly is OK in oython instead of precompiling
            # No performance hit expected
            self.player_colors[player] = color
        else:
            print('Unexpected token')

    # x and y start on 0 and go till row - 1 and col - 1 respectively
    def make_move(self, x, y):
        if(x >= 0 and x < self.row and y >= 0 and y < self.col):
            # If it is 'o' then the user clicked on a new tile else an existing one
            if(self.game[x][y] == 'o'):
                if(self.board[x][y] == 'o'):
                    self.game[x][y] = self.revealed[x][y]
                    self.player = (self.player + 1)%2
                else:
                    self.game[x][y] = -self.player - 1
        else:
            print('Invalid input at x:'+str(x)+' y:'+str(y))

    def get_grid(self):
        my_grid = []
        for row in range(0, self.row):
            my_grid.append([])
            for col in range(0, self.col):
                if(self.game[row][col] >= 0):
                    my_grid[row].append(self.game[row][col])
                else:
                    my_grid[row].append(self.player(-1 -self.game[row][col]))
        return my_grid

    # Implement win criteria here
    def win_criteria(self, x):
        return



my_obj = board()
my_obj.pretty_print_chars()
my_obj.pretty_print_grid()
