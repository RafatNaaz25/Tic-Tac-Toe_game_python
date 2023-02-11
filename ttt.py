def print_board(board):
    print('\n'.join([' '.join([str(cell) for cell in row]) for row in board]))

def make_move(board, player, row, col):
    if row < 0 or row > 2 or col < 0 or col > 2:
        return False
    if board[row][col] != '_':
        return False
    board[row][col] = player
    return True

def has_won(board, player):
    for row in board:
        if row == [player, player, player]:
            return True
    for col in range(3):
        if [board[0][col], board[1][col], board[2][col]] == [player, player, player]:
            return True
    if [board[0][0], board[1][1], board[2][2]] == [player, player, player]:
        return True
    if [board[2][0], board[1][1], board[0][2]] == [player, player, player]:
        return True
    return False

def tic_tac_toe():
    board = [['_' for _ in range(3)] for __ in range(3)]
    players = ['X', 'O']
    current_player = 0
    while True:
        print_board(board)
        print(f'Player {players[current_player]} turn')
        row = int(input('Enter row: '))
        col = int(input('Enter col: '))
        if not make_move(board, players[current_player], row, col):
            print('Invalid move')
            continue
        if has_won(board, players[current_player]):
            print_board(board)
            print(f'Player {players[current_player]} has won!')
            break
        current_player = (current_player + 1) % 2

if __name__ == '__main__':
    tic_tac_toe()



