from itertools import combinations

def solution(relation):
    answer = 0
    atnum = len(relation[0])
    attributes = set([i for i in range(atnum)])
    keysize = 1
    candidate = []
    while keysize <= len(attributes):
        for i in combinations(attributes,keysize):
            contain = []
            for j in relation:
                temp = []
                for k in i:
                    temp.append(j[k])
                if (temp in contain) == False:
                    contain.append(temp)
                else:
                    break
            if len(contain) == len(relation):
                check = True
                for k in range(1,keysize+1):
                    for l in combinations(i,k):
                        if (l in candidate):
                            check = False
                            break
                if check:
                    answer += 1
                    candidate.append(i[:])
        keysize += 1
    return answer