def solution(picks, minerals):
    # 22:19
    # 22:37
    # 좀 더 침착하게 코딩중 실수를 줄여야할듯??
    # 그리고 주어진 데이터의 수가 작으면 브루트 포스 방법도 아주 좋다
    mineralIndex = {"diamond":0, "iron":1, "stone":2}
    tireTable = [[1,1,1],[5,1,1],[25,5,1]]
    picks.append(0)
    cur = [picks]
    index = 0
    while index < len(minerals):
        temp = []
        for d, i, s, t in  cur:
            if d != 0:
                tempTire = 0
                for m in range(index, index + 5):
                    if m >= len(minerals):
                        break
                    tempTire += tireTable[0][mineralIndex[minerals[m]]]
                temp.append([d-1,i,s,t+tempTire])
            if i != 0:
                tempTire = 0
                for m in range(index, index + 5):
                    if m >= len(minerals):
                        break
                    tempTire += tireTable[1][mineralIndex[minerals[m]]]
                temp.append([d,i-1,s,t+tempTire])
            if s != 0:
                tempTire = 0
                for m in range(index, index + 5):
                    if m >= len(minerals):
                        break
                    tempTire += tireTable[2][mineralIndex[minerals[m]]]
                temp.append([d,i,s-1,t+tempTire])
        if len(temp) == 0:
            break
        cur = temp
        index += 5
    cur.sort(key=lambda x : x[3])

    return cur[0][3]
