def solution(board, moves):
    answer = 0
    dolls = []
    dump = []
    for i in range(len(board)):
        temp = []
        for j in range(len(board) - 1, -1, -1):
            if board[j][i] != 0:
                temp.append(board[j][i])
            else:
                break
        dolls.append(temp)
    for i in moves:
        if dolls[i - 1] != []:
            value = dolls[i - 1].pop()
            if dump == []:
                dump.append(value)
            elif value == dump[len(dump) - 1]:
                answer += 2
                dump.pop()
            else:
                dump.append(value)

    return answer