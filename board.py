#!/usr/bin/python
import random

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
        self.TwoP = []
        self.row = row
        self.col = col
        self.total = total

        # Initialize to 0s
        self.revealed = [[0 for x in range(col)] for y in range(row)]
        numerator = total
        denominator = row * col

        # -1 = Bomb
        # 0-8 = Numbers in grid
        for x in range(0, row):
            self.board.append([])
            self.TwoP.append([])
            self.revealed.append([])
            for y in range(0, col):
                if( random.random() < (1.0 * numerator/denominator) ):
                    self.board[x].append('x')
                    self.revealed[x][y] = -1
                    self.__update_cell(x, y)
                    numerator -= 1
                else:
                    self.board[x].append('o')
                self.TwoP.append(' ')
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

    def make_move (this, index , operation):
        return

    def get_grid(this):
        return




my_obj = board()
my_obj.pretty_print_chars()
my_obj.pretty_print_grid()