def solution(board):
    # 17:34
    # 17:51
    curLoc = [0,0]
    dest = [0,0]
    visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R":
                curLoc = [i, j]
                visited[i][j] = 1
            if board[i][j] == "G":
                dest = [i, j]
    nextNode = [curLoc]
    answer = 0

    possible = False
    while nextNode:
        temp = []
        for i, j in nextNode:
            for nextI, nextJ in can_go(i, j, board, visited):
                visited[nextI][nextJ] = 1
                temp.append([nextI, nextJ])
        answer += 1
        if visited[dest[0]][dest[1]] == 1:
            possible = True
            break
        nextNode = temp

    if possible:
        return answer
    else:
        return -1

def can_go(i, j, board, visited):
    result = []
    topIndex = i
    while topIndex - 1 >= 0:
        if board[topIndex-1][j] != "D":
            topIndex -= 1
        else:
            break
    if visited[topIndex][j] == 0:
        result.append([topIndex, j])

    bottomIndex = i
    while bottomIndex + 1 < len(board):
        if board[bottomIndex+1][j] != "D":
            bottomIndex += 1
        else:
            break
    if visited[bottomIndex][j] == 0:
        result.append([bottomIndex, j])

    leftIndex = j
    while leftIndex - 1 >= 0:
        if board[i][leftIndex - 1] != "D":
            leftIndex -= 1
        else:
            break
    if visited[i][leftIndex] == 0:
        result.append([i, leftIndex])

    rightIndex = j
    while rightIndex + 1 < len(board[0]):
        if board[i][rightIndex + 1] != "D":
            rightIndex += 1
        else:
            break
    if visited[i][rightIndex] == 0:
        result.append([i, rightIndex])

    return result
