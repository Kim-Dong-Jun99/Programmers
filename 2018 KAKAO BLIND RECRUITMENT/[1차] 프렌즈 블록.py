def solution(m, n, board):
    answer = 0
    play = True
    while play:
        target = []
        play = False
        for i in range(m):
            for j in range(n):
                if canBomb(i, j, board):
                    target.append([i, j])
                    play = True
        for i in target:
            board = bomb(i[0], i[1], board)
        board = afterBomb(board)
        print(board)
    for i in range(m):
        for j in range(n):
            if board[i][j].isdigit():
                answer += 1

    return answer


def canBomb(i, j, board):
    if i + 1 < len(board):
        if j + 1 < len(board[0]):
            if board[i][j].isalpha():
                if board[i][j] == board[i + 1][j + 1] and board[i][j] == board[i + 1][j] and board[i][j] == board[i][
                    j + 1]:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def bomb(i, j, board):
    # board[i][j] = '0'
    board[i] = board[i][:j] + '0' + board[i][j + 1:]
    # board[i+1][j] = '0'
    board[i + 1] = board[i + 1][:j] + '0' + board[i + 1][j + 1:]
    # board[i][j+1] = '0'
    board[i] = board[i][:j + 1] + '0' + board[i][j + 2:]
    # board[i+1][j+1] = '0'
    board[i + 1] = board[i + 1][:j + 1] + '0' + board[i + 1][j + 2:]
    return board


def afterBomb(board):
    for j in range(len(board[0])):
        i = len(board) - 1
        while i > -1:
            if board[i][j].isdigit():
                k = i - 1
                while k > -1:
                    if board[k][j].isalpha():
                        board[i] = board[i][:j] + board[k][j] + board[i][j + 1:]
                        board[k] = board[k][:j] + '0' + board[k][j + 1:]
                        break
                    else:
                        k -= 1
            i -= 1

    return board





