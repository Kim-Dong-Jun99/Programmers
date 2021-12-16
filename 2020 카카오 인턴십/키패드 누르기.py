def solution(numbers, hand):
    answer = ''
    table = {}
    useLeft = [1, 4, 7]
    useRight = [3, 6, 9]
    lloc = [3, 0]
    rloc = [3, 2]
    for i in range(4):
        if i != 3:
            for j in range(3):
                table[i * 3 + j + 1] = [i, j]
        else:
            table[0] = [3, 1]
    for i in numbers:
        if (i in useLeft):
            answer += 'L'
            lloc = table[i]
        elif (i in useRight):
            answer += 'R'
            rloc = table[i]
        else:
            temp = table[i]
            ldis = abs(temp[0] - lloc[0]) + abs(temp[1] - lloc[1])
            rdis = abs(temp[0] - rloc[0]) + abs(temp[1] - rloc[1])
            if ldis < rdis:
                answer += 'L'
                lloc = table[i]
            elif rdis < ldis:
                answer += 'R'
                rloc = table[i]
            else:
                if hand == 'right':
                    answer += 'R'
                    rloc = table[i]
                else:
                    answer += 'L'
                    lloc = table[i]

    return answer