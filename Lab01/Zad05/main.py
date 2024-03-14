# by Crowfunder
# I do not feel regret for any mess I've made.
# This is pre-hackathon training.

# This is ultra cursed tic tac toe game.
# It's mostly normal, except for the fact that thanks
# to a small debate I had with my colleagues I decided
# that the only viable way to determine which figure starts
# will be polling NASA telmetry data from a few satellites
# and doing modulo 2 on the hash() of received data.
# This is borderline insanity, I love it with all my heart.

import requests

def ListFlatten(list):
    return [item for sublist in list for item in sublist]  

class Board:
    def __init__(self):
        # Indexes are [x][y]
        self.board_data = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        # for tests
        #self.board_data = [['X',' ','X'],['X','X','O'],['O','O','X']]


    def CreateBoard(self):
        board = '\n-------------\n'
        for y in range(3):
            for x in range(3):
                board += f'| {self.board_data[x][y]} '
            board += '|'
            board += '\n-------------\n'
        return board


    def Move(self, x, y, player):
        
        # humans start counting from 1
        x-=1
        y-=1
        try:
            if self.board_data[x][y] == ' ':
                self.board_data[x][y] = player
                return True
        except IndexError:
            pass
        return False

    # Detects victory or impasse
    def BoardWatchdog(self):

        # Check rows
        for y in range(3):
            row = []
            for x in range(3):
                row.append(self.board_data[x][y])
            if row[0] != ' ' and row.count(row[0]) == 3:
                return row[0]

        # Check columns
        for x in range(3):
            column = []
            for y in range(3):
                column.append(self.board_data[x][y])
            if column[0] != ' ' and column.count(column[0]) == 3:
                return column[0]

        # Check for diagonals
        diagonal1 = [self.board_data[0][0], self.board_data[1][1], self.board_data[2][2]]
        diagonal2 = [self.board_data[2][0], self.board_data[1][1], self.board_data[0][2]]
        if diagonal1[0] != ' ' and diagonal1.count(diagonal1[0]) == 3:
            return diagonal1[0]
        if diagonal2[0] != ' ' and diagonal2.count(diagonal2[0]) == 3:
            return diagonal2[0]

        # Check for impasse
        if ' ' not in ListFlatten(self.board_data):
            return 'Impasse'

        return None


def StartPlayer():
    try:
        response = requests.get('https://tle.ivanstanojevic.me/api/tle/')
        if response.status_code == 200:
            return hash(response) % 2
        else:
            return 0
    except:
        return 0

def main():
    board = Board()
    turn = 0

    if StartPlayer() == 0:
        players = {'O':'Kółko', 'X':'Krzyżyk'}
    else:
        players = {'X':'Krzyżyk', 'O':'Kółko'}

    while True:
        for player, name in players.items():
            turn += 1
            print(board.CreateBoard())

            print('__________________')
            print(f'Tura numer: {turn}')

            # Call BoardWatchdog() to check if the game is over
            turn_result = board.BoardWatchdog()
            if turn_result:
                if turn_result == 'Impasse':
                    print('Remis!')
                    return
                print(f'Wygrał gracz {players[turn_result]}')
                return

            print(f'Ruch gracza: {name}')
            print('__________________')

            while True:
                try:
                    move_x = int(input('Podaj kolumne: '))
                    move_y = int(input('Podaj wiersz: '))
                except ValueError:
                    print('Podaj poprawną wartość!')
                    continue
                
                if board.Move(move_x, move_y, player):
                    break
                print('Niepoprawne pole')

if __name__ == '__main__':
    main()
        