def solution(p):
    answer = ''
    if p == '':
        return p
    elif checkvalid(p):
        return p
    else:
        i = 2
        while i <= len(p):
            if p[:i].count('(') == p[:i].count(')'):
                break
            else:
                if i == len(p):
                    break
                i += 2
        u = p[:i]
        v = p[i:]
        if checkvalid(u):
            answer = u + solution(v)
        else:
            u = u[1:len(u) - 1]
            temp = ''
            if u != '':
                for i in range(len(u)):
                    if u[i] == '(':
                        temp += ')'
                    else:
                        temp += '('

            answer = '(' + solution(v) + ')' + temp
    return answer


def checkvalid(str):
    stack = []
    for i in str:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack == []:
        return True
    else:
        return False