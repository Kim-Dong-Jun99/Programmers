def solution(m, n, startX, startY, balls):
    # 22:02
    # 23:14
    """
    m = 당구대의 가로 길이
    n = 당구대의 세로 길이
    공위치 = startX, startY
    칠 공들 = balls
    벽 순서 = 동서남북으로 하쟈
    """
    answer = []

    for ballX, ballY in balls:
        temp = []
        points = getPoints(ballX, ballY, startX, startY, m, n)
        for px, py in points:
            if checkCorner(startX, startY, px, py, m, n):
                continue
            temp.append(calc_dis(startX, startY, px, py))
        answer.append(min(temp))


    return answer
# a, b = 맞출 공
def getPoints(a, b, c, d, m, n):
    result = []
    if (b == d):
        if a > c:
            # eastP = [m + (m-a),n]
            westP = [-a,b]
            southP = [a,-b]
            northP = [a, n + (n-b)]
            # result.append(eastP)
            result.append(westP)
            result.append(southP)
            result.append(northP)
        else:
            eastP = [m + (m-a),b]
            # westP = [-a,n]
            southP = [a,-b]
            northP = [a, n + (n-b)]
            result.append(eastP)
            # result.append(westP)
            result.append(southP)
            result.append(northP)

    elif (a == c):
        if d > b:
            eastP = [m + (m-a),b]
            westP = [-a,b]
            # southP = [a,-b]
            northP = [a, n + (n-b)]
            result.append(eastP)
            result.append(westP)
            # result.append(southP)
            result.append(northP)
        else:
            eastP = [m + (m-a),b]
            westP = [-a,b]
            southP = [a,-b]
            # northP = [a, n + (n-b)]
            result.append(eastP)
            result.append(westP)
            result.append(southP)
            # result.append(northP)
    else:
        eastP = [m + (m-a),b]
        westP = [-a,b]
        southP = [a,-b]
        northP = [a, n + (n-b)]
        result.append(eastP)
        result.append(westP)
        result.append(southP)
        result.append(northP)

    return result

def checkCorner(startX, startY, px, py, m, n):
    if startX == px:
        return False
    dsw = (startY - py)/(startX - px)
    sw = startY -  dsw * startX
    if sw == 0:
        return True
    dnw = (startY - py)/(startX - px)
    nw = startY - dnw * startX
    if nw == n:
        return True
    dne = (startY - py)/(startX - px)
    ne = startY - dne * startX
    if ne+m*dne == n:
        return True
    dse = (startY - py)/(startX - px)
    se = startY - dse * startX
    if se+m*dse == 0:
        return True
    return False

def calc_dis(i,j,x,y):
    return (i-x)**2 + (j-y)**
