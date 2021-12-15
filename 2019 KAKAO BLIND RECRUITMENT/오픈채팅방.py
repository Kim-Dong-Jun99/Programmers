def solution(record):
    answer = []
    table = {}
    for i in range(len(record)):
        query = list(record[i].split())
        if query[0] == 'Enter' or query[0] == 'Change':
            table[query[1]] = query[2]
    for i in range(len(record)):
        query = list(record[i].split())
        if query[0] == 'Enter':
            temp = '님이 들어왔습니다.'
            answer.append(table[query[1]]+temp)
        elif query[0] == "Leave":
            temp = '님이 나갔습니다.'
            answer.append(table[query[1]]+temp)
    return answer