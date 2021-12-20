def solution(s):
    answer = []
    tuples = []
    s = s[1:len(s) - 1]
    temp = []
    i = 0
    while i < len(s):
        if s[i] == '}':
            if tuples == []:
                tuples.append(temp)
            else:
                j = 0
                compare = len(temp)
                while j < len(tuples):
                    if len(tuples[j]) > compare:
                        tuples.insert(j, temp)
                        break
                    elif j == len(tuples) - 1:
                        tuples.append(temp)
                        break
                    else:
                        j += 1
            temp = []
            i += 1
        elif s[i].isdigit():
            j = i
            while j < len(s):
                if s[j].isdigit():
                    j += 1
                else:
                    break
            temp.append(int(s[i:j]))
            i = j
        else:
            i += 1

    for i in tuples:
        if answer == []:
            answer.append(i[0])
        else:
            temp = set(answer)
            temp2 = set(i)
            diff = list(temp2.difference(temp))
            answer.append(diff.pop())
    return answer