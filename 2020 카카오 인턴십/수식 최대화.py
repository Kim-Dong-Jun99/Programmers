from itertools import permutations


def solution(stanexpression):
    calc = ['+', '-', '*']
    values = []
    for i in list(permutations(calc, 3)):
        expression = stanexpression[:]
        for j in i:
            k = 0
            while k < len(expression):
                if expression[k] == j and k != 0:
                    left = k - 1
                    right = k + 2
                    while 0 <= left:
                        if expression[left].isdigit():
                            if left == 0:
                                break
                            left -= 1
                        else:
                            left += 1
                            break
                    while right < len(expression):
                        if expression[right].isdigit():
                            right += 1
                        else:
                            break
                    if 0 < left and expression[left - 1] == '-':
                        if left - 1 == 0 or expression[left - 2].isdigit() == False:
                            left -= 1
                    leftvalue = int(expression[left:k])
                    rightvalue = int(expression[k + 1:right])
                    if j == '+':
                        temp = leftvalue + rightvalue
                    elif j == '*':
                        temp = leftvalue * rightvalue
                    else:
                        temp = leftvalue - rightvalue
                    expression = expression[:left] + str(temp) + expression[right:]
                    k = left + 1
                else:
                    k += 1
        values.append(abs(int(expression)))

    return max(values)