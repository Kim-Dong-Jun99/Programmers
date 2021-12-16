def solution(rows, columns, queries):
    answer = []
    matrix = []
    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(i*columns+j+1)
        matrix.append(temp)
    for i in queries:
        values = []
        startIndex = [i[0]-1,i[1]-1]
        endIndex = [i[2]-1,i[3]-1]
        queue = [matrix[startIndex[0]][startIndex[1]]]
        values.append(matrix[startIndex[0]][startIndex[1]])
        j = startIndex[1]+1
        while j <= endIndex[1]:
            queue.append(matrix[startIndex[0]][j])
            values.append(matrix[startIndex[0]][j])
            matrix[startIndex[0]][j] = queue.pop(0)
            j += 1
        j = startIndex[0]+1
        while j <= endIndex[0]:
            queue.append(matrix[j][endIndex[1]])
            values.append(matrix[j][endIndex[1]])
            matrix[j][endIndex[1]] = queue.pop(0)
            j += 1
        j = endIndex[1]-1
        while j >= startIndex[1]:
            queue.append(matrix[endIndex[0]][j])
            values.append(matrix[endIndex[0]][j])
            matrix[endIndex[0]][j] = queue.pop(0)
            j -= 1
        j = endIndex[0]-1
        while j >= startIndex[0]:
            queue.append(matrix[j][startIndex[1]])
            values.append(matrix[j][startIndex[1]])
            matrix[j][startIndex[1]] = queue.pop(0)
            j -= 1
        answer.append(min(values))
    return answer