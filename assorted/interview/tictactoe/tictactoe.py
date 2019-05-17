#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" replace CR with LF """
import sys


class Board():
    def __init__(self):
        self.board = ['-'] * 9

    def draw(self):
        print(self.board[0], '|', self.board[1], '|', self.board[2])
        print(self.board[3], '|', self.board[4], '|', self.board[5])
        print(self.board[6], '|', self.board[7], '|', self.board[8])
        print('===========')
        print()

    def add_token(self, loc: int, token: str = 'X'):
        if self.board[loc] == '-':
            self.board[loc] = token
        self.draw()
        pass


b = Board()
b.add_token(4, 'X')
b.draw()

# for i in range(100000):

# self.board = []
# self.board = '-' * 9
# print(board[0], '|', board[1], '|', board[2])
# print(board[3], '|', board[4], '|', board[5])
# print(board[6], '|', board[7], '|', board[8])
