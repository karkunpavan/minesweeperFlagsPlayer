#!/usr/bin/python
import random

class board(object):
    def __init__(self, row = 16, col = 16, total = 51):
        self.board = []
        numerator = 51
        denominator = row * col
        for x in range(0, row):
            self.board.append([])
            for y in range(0, col):
                if( random.random() < (1.0 * numerator/denominator) ):
                    self.board[x].append('x')
                    numerator -= 1
                else:
                    self.board[x].append('o')
                denominator -= 1

    def pretty_print(self):
        lenr = len(self.board)
        lenc = len(self.board[1])
        for row in range(0,lenr):
            my_str = ''
            for col in range(0,lenc):
                my_str += self.board[row][col]
            print(my_str)


my_obj = board()
my_obj.pretty_print()