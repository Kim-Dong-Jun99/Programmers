def solution(places):
    answer = []
    for itr in range(len(places)):
        room = places[itr][:]
        status = None
        for i in range(len(room)):
            for j in range(len(room)):
                if room[i][j] == 'P':
                    if ('P' in room[i][j + 1:j + 3]):
                        if room[i][j + 1] != 'X':
                            status = 0
                            break
                    if i + 1 < len(room) and j + 1 < len(room):
                        if room[i + 1][j + 1] == 'P':
                            if room[i + 1][j] != 'X' or room[i][j + 1] != 'X':
                                status = 0
                                break
                    if i + 1 < len(room) and -1 < j - 1:
                        if room[i + 1][j - 1] == 'P':
                            if room[i][j - 1] != 'X' or room[i + 1][j] != 'X':
                                status = 0
                                break
                    if i + 2 < len(room):
                        if room[i + 1][j] == 'P' or room[i + 2][j] == 'P':
                            if room[i + 1][j] != 'X':
                                status = 0
                                break
                    if i == len(room) - 2:
                        if room[i + 1][j] == 'P':
                            status = 0
                            break
        if status == None:
            answer.append(1)
        else:
            answer.append(0)

    return answer