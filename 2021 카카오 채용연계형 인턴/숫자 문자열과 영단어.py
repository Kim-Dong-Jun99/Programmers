def solution(s):
    answer = ''
    i = 0
    table = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
             'eight': '8', 'nine': '9'}
    while i < len(s):
        if 97 <= ord(s[i]) and ord(s[i]) <= 122:
            j = i
            temp = ''
            while 97 <= ord(s[j]) and ord(s[j]) <= 122 and j < len(s):

                temp += s[j]
                j += 1
                if (temp in table):
                    break
            answer += table[temp]
            i = j
        else:
            answer += s[i]
            i += 1
    return int(answer)