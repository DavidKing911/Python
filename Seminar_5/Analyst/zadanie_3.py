# Создайте программу для игры в ""Крестики-нолики"".
from os import system
system("cls")
import random

def get_number(input_string):
    while True:
        try:
            num = int(input(input_string))
            if 0 <= num < 3:
                return num
            else:
                print('Неправильно. Давай еще раз.')
        except ValueError:
            print('Это не то ...')

def get_player(player_0, player_1):
    temp = random.randint(0, 1)
    if temp == 0:
        gamer = player_0
    else:
        gamer = player_1
    print(f'Первый ходит: {gamer}!')
    return gamer

def get_mark(input_string):
    while True:
        try:
            mark = input(input_string)
            if mark in 'xoXO':
                mark_0 = mark.upper()
                if mark_0 == 'X':
                    mark_1 = 'O'
                else:
                    mark_1 = 'X'
                return mark_0, mark_1
            else:
                print('Неправильно. Давай еще раз.')
        except ValueError:
            print('Это не то ...')

def board_draw(board):
    print (" —-----------")
    for i in range(3):
        print (f" |", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print (" —-----------")

def winner(board):
    for i in range(3):
        if (board[i][0] == board[i][1] and board[i][0] == board[i][2]) and board[i][0] != ' ':
            return True
    for i in range(3):
        if (board[0][i] == board[1][i] and board[0][i] == board[2][i]) and board[0][i] != ' ':
            return True
    if (board[0][0] == board[1][1] and board[0][0] == board[2][2]) and board[1][1] != ' ':
        return True
    if (board[0][2] == board[1][1] and board[0][2] == board[2][0]) and board[1][1] != ' ':
        return True
    return False

def draw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

def play_game(gamer, name_player_1, name_player_2, sign_0, sign_1, game_board):
    while True:
        if gamer == name_player_1:
            ind_2 = get_number('Введите координату "Х" клетки:\n')
            ind_1 = get_number('Введите координату "Y" клетки:\n')
            if game_board[ind_1][ind_2] == ' ':
                game_board[ind_1][ind_2] = sign_0
                board_draw(game_board)
                if winner(game_board):
                    text = (f'{gamer} победил')
                    return text
                gamer = name_player_2
        else:
            ind_2 = random.randint(0, 2)
            ind_1 = random.randint(0, 2)
            if game_board[ind_1][ind_2] == ' ':
                game_board[ind_1][ind_2] = sign_1
                board_draw(game_board)
                if winner(game_board):
                    text = (f'{gamer} победил')
                    return text
                gamer = name_player_1
        if draw(game_board):
            return 'Ничья'

playing_field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
print('Это игра "Крестики-нолики"')
name_0 = input('Введите ваше имя: \n')
mark_0, mark_1 = get_mark('Выберите крестик - х или нолик - о:\n')
name_1 = 'Бот'
gamer_int = get_player(name_0, name_1)
board_draw(playing_field)
print(play_game(gamer_int, name_0, name_1, mark_0, mark_1, playing_field))