from itertools import combinations


def solution(relation):
    answer = 0
    atnum = len(relation[0])
    attributes = set([i for i in range(atnum)])
    keysize = 1
    while keysize <= len(attributes):
        remove = set()
        for i in combinations(attributes, keysize):
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
                answer += 1
                for j in i:
                    remove.add(j)
        attributes = attributes.difference(remove)

        keysize += 1
    return answer