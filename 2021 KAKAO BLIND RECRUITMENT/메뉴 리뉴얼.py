from itertools import combinations


def solution(orders, course):
    answer = []

    for i in course:
        tempSet = set()
        temp = []
        for j in orders:
            if len(j) >= i:
                for k in list(combinations(j, i)):
                    tempstr = ''
                    k = list(k)
                    k.sort()
                    for l in k:
                        tempstr += l
                    tempSet.add(tempstr)
                    temp.append(tempstr)
        maximumAppearance = []
        for j in tempSet:
            if temp.count(j) >= 2:
                if maximumAppearance == []:
                    maximumAppearance.append(j)
                else:
                    if temp.count(j) > temp.count(maximumAppearance[0]):
                        while maximumAppearance:
                            maximumAppearance.pop()
                        maximumAppearance.append(j)
                    elif temp.count(j) == temp.count(maximumAppearance[0]):
                        maximumAppearance.append(j)

        answer += maximumAppearance
    answer.sort()
    return answer