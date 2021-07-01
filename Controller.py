import collections
import random
import Player

import csv
import requests
import xml.etree.ElementTree as ET

from Property import Property, Location, Transport, Utility, Special, Go, CommunityChest, Chance, Tax, Jail, FreeSpace, \
    GoToJail


def roll_dice():
    value = random.randint(1, 6)
    return value


def roll_two():
    val1 = roll_dice()
    val2 = roll_dice()
    val = val1 + val2
    return val, (val1 == val2)


def init_board():
    GO = Go()
    community_chest = CommunityChest()
    chance = Chance()
    income_tax = Tax("Income Tax", "ITX", 100)
    super_tax = Tax("Super Tax", "STX", 200)
    jail = Jail()
    free_space = FreeSpace()
    go_to_jail = GoToJail()

    player_board = [[("", [" "]), ("", [" "]), ("", [" "]), ("", [" "]), ("", [" "]), ("", [" "]), ("", [" "]), ("", [" "]), ("", [" "]), ("", [" "]), ("", [" "])],
             [("", [" "]), "", "", "", "", "", "", "", "", "", ("", [" "])],
             [("", [" "]), "", "", "", "", "", "", "", "", "", ("", [" "])],
             [("", [" "]), "", "", "", "", "", "", "", "", "", ("", [" "])],
             [("", [" "]), "", "", "", "", "", "", "", "", "", ("", [" "])],
             [("", [" "]), "", "", "", "", "", "", "", "", "", ("", [" "])],
             [("", [" "]), "", "", "", "", "", "", "", "", "", ("", [" "])],
             [("", [" "]), "", "", "", "", "", "", "", "", "", ("", [" "])],
             [("", [" "]), "", "", "", "", "", "", "", "", "", ("", [" "])],
             [("", [" "]), "", "", "", "", "", "", "", "", "", ("", [" "])],
             [("", [" "]), ("", [" "]), ("", [" "]), ("", [" "]), ("", [" "]), ("", [" "]), ("", [" "]), ("", [" "]), ("", [" "]), ("", [" "]), ("", [" "])],
             ]
    return player_board

#TODO: Reset board to exist with 0,0 top left instead of 1,1

def init_players(player_list, board):
    name_list = []
    for i in player_list:
        name_list.append(i.get_name())
    board[10][10] = name_list
    return board


def change_player_xy(move_amount, player_x, player_y):
    if player_x == 1 and not player_y == 1:
        if move_amount > player_y - 1:
            return change_player_xy(move_amount - player_y + 1, 1, 1)
        else:
            player_y = player_y - move_amount
            return player_x, player_y
    if player_x == 11 and not player_y == 11:
        if move_amount > 11 - player_y:
            return change_player_xy(move_amount - (11 - player_y), 11, 11)
        else:
            player_y = player_y + move_amount
            return player_x, player_y
    if player_y == 11 and not player_x == 1:
        if move_amount > player_x - 1:
            return change_player_xy(move_amount - player_x + 1, 1, 11)
        else:
            player_x = player_x - move_amount
            return player_x, player_y
    if player_y == 1 and not player_x == 11:
        if move_amount > 11 - player_x:
            return change_player_xy(move_amount - (11 - player_x), 11, 1)
        else:
            player_x = player_x + move_amount
            return player_x, player_y


def update_board(player_x, player_y, old_x, old_y, board, player):
    if len(board[old_y - 1][old_x - 1]) == 1:
        board[old_y - 1][old_x - 1] = [" "]
    else:
        board[old_y - 1][old_x - 1].remove(player.get_name())
    if len(board[player_y - 1][player_x - 1]) == 1 and board[player_y - 1][player_x - 1] == [" "]:
        board[player_y - 1][player_x - 1] = [player.get_name()]
    else:
        board[player_y - 1][player_x - 1].append(player.get_name())
    return board


def update_board(board, player_list):



def place_player(player_x, player_y, player, board):
    board[player_y - 1][player_x - 1] = [player]
    return board


def move_player(player, board, count=1):
    move_amount, double_roll = roll_two()
    new_x, new_y = change_player_xy(move_amount, player.get_x(), player.get_y())
    board = update_board(new_x, new_y, player.get_x(), player.get_y(), board, player)
    player.set_x(new_x)
    player.set_y(new_y)
    if double_roll and count < 2:
        return move_player(player, board, count + 1)
    else:
        return board


def print_board(board):
    for i in board:
        print(i)


def parse_properties():
    location_list = []
    transport_list = []
    utility_list = []
    tree = ET.parse("Properties.xml")
    root = tree.getroot()
    for i in root:
        if i.tag == "location":
            location_list.append(Location(i[0].text, i[1].text, i[2].text, i[3].text, i[4].text, i[5].text, i[6].text, i[7].text, i[8].text, i[9].text, i[10].text, i[11].text))
        if i.tag == "transport":
            transport_list.append(Transport(i[0].text, i[1].text, i[2].text, i[3].text, i[4].text, i[5].text, i[6].text))
        if i.tag == "utility":
            utility_list.append(Utility(i[0].text, i[1].text, i[2].text, i[3].text, i[4].text))
    #print(root)
    for i in location_list:
        print(i)
    #print(len(location_list))


def main():
    player = Player.Player("P")
    board = init_board()
    #board = init_players(player_list, board)
    board = move_player(player, board)
    parse_properties()


if __name__ == "__main__":
    main()

