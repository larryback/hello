#!/usr/bin/python
#-*- coding: utf-8 -*-

from Game import Game

if __name__ == '__main__':
    print("Welcom to Black Jack.")
    while True:
        blackjack = Game()
        blackjack.fn_start()

        ans = input('Are you continue (yes or no) ? ')
        if ans != 'yes':
            break;
    
    print("Bye !, See you again.")


