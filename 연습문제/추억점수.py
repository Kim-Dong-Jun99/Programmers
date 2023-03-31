def solution(name, yearning, photo):
    # 21:30 시작시간
    # 21:33 종료시간
    answer = []
    score = {}
    for i in range(len(name)):
        score[name[i]] = yearning[i]
    for p in photo:
        result = 0
        for temp in p:
            if temp in score:
                result += score[temp]
        answer.append(result)
    
    return answer