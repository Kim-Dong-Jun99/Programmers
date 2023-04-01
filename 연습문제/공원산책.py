def solution(park, routes):
    # 11:18
    # 11:35
    # 더 천천히 풀었으면 오히려 더 빨랐을듯
    dTable = {"E":(0,1),"S":(1,0),"W":(0,-1),"N":(-1,0)}
    curLoc = [0,0]
    row = len(park)
    col = len(park[0])
    for i in range(row):
        for j in range(col):
            if park[i][j] == "S":
                curLoc = [i,j]
                break
    for route in routes:
        direction, distance = route.split()
        direction = dTable[direction]
        distance = int(distance)
        cantgo = False
        for i in range(1,distance+1):
            if curLoc[0] + direction[0] * i >= row or curLoc[1] + direction[1] * i >= col or curLoc[0] + direction[0]*i < 0 or curLoc[1] + direction[1]*i < 0:
                cantgo = True
                break
            if park[curLoc[0]+direction[0] * i][curLoc[1]+direction[1]*i] == "X":
                cantgo = True
                break
        if cantgo:
            continue
        else:
            curLoc[0] += direction[0]*distance
            curLoc[1] += direction[1]*distance



    return curLoc
