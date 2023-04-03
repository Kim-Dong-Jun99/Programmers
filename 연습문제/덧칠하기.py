def solution(n, m, section):
    answer = 0
    """
    13:05
    13:11
    """
    index = 0
    while index < len(section):
        left = section[index]

        while index < len(section) and left + m - 1 >= section[index]:
            index += 1
        answer += 1
    return answer
