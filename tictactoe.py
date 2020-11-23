from Modules.ClassBoard import Board
from Modules.ClassPlayer import Player

if __name__ == '__main__':
    player_1 = Player(1)
    player_2 = Player(-1)
    board = Board()
    active_player = player_1

    while not board.is_full():
        board.print_board()
        try:
            cell = int(input("Wo willst du den Zeichen setzen? (Zahl 1 - 9)"))
        except ValueError:
            continue
        cell = cell - 1
        if cell < 0 or cell > 8:
            print("Bitte gib eine Zahl zwischen 1 und 9 an!") 
            continue
        if not board.make_turn(cell, active_player):
            print("das Feld ist bereits Vergeben!")
            continue

        if board.check_win(active_player):
            print(board.print_board())
            print("Du hast Gewonnen! GG!")
            exit()

        if active_player == player_1:
            active_player = player_2
        else:
            active_player = player_1
