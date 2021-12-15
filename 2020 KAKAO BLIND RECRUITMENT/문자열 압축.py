def solution(s):
    answer = None
    for i in range(1,int(len(s)/2)+1):
        temp = []
        index = 0
        while index < len(s):
            if index + i > len(s):
                temp.append(s[index:])
            else:
                temp.append(s[index:index+i])
            index += i
        tempResult = 0
        j = 0
        while j < len(temp):
            if j != len(temp)-1 and temp[j] == temp[j+1]:
                k = j
                while k < len(temp):
                    if temp[j] == temp[k]:
                        k += 1
                    else:
                        break
                reduced = len(temp[j])+len(str(k-j))
                if reduced < len(temp[j])*(k-j):
                    tempResult += reduced
                    j = k
                else:
                    tempResult += len(temp[j])
                    j += 1
            else:
                tempResult += len(temp[j])
                j += 1

        if answer == None:
            answer = tempResult
        elif answer > tempResult:
            answer = tempResult

    if answer == None:
        answer = len(s)
    return answer