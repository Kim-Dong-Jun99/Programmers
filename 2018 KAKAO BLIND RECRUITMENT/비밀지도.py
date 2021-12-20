def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        temp1 = bin(arr1[i])
        temp2 = bin(arr2[i])
        temp1 = temp1[2:]
        temp2 = temp2[2:]
        while len(temp1) < n:
            temp1 = '0'+temp1
        while len(temp2) < n:
            temp2 = '0'+temp2
        ans = ''
        for j in range(len(temp1)):
            if temp1[j] == '1' or temp2[j] == '1':
                ans += '#'
            else:
                ans += ' '
        answer.append(ans)
    return answer