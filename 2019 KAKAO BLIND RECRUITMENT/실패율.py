def solution(N, stages):
    answer = []
    count = [0 for i in range(N+2)]
    for i in stages:
        count[i] += 1
    player = len(stages)
    unpassed = 0
    for i in range(1,N+1):
        if count[i] != 0:
            temp = count[i]
            count[i] = (count[i]/(player-unpassed))
            unpassed += temp
            if answer == []:
                answer.append(i)
            else:
                j = 0
                while j < len(answer):
                    if count[i] > count[answer[j]]:
                        answer.insert(j,i)
                        break
                    elif j == len(answer)-1:
                        answer.append(i)
                        break
                    else:
                        j += 1
        else:
            answer.append(i)
    return answer