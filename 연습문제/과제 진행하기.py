def solution(plans):
    # 21:40
    # 22:26
    # 문제 조건을 좀 더 꼼꼼히 읽었으면 30분 안쪽으로 풀지 않았을까?
    answer = []
    newPlans = []
    for work in plans:
        temp_ = []
        temp_.append(work[0])
        time = work[1].split(":")
        temp_.append(int(time[0]) * 60 + int(time[1]))
        temp_.append(int(work[2]))
        newPlans.append(temp_)
    newPlans.sort(key=lambda x : x[1])
    # print(newPlans)
    stack = []
    curTime = 0
    for work in newPlans:
        if len(stack) == 0:
            stack.append(work)
            curTime = work[1]
        else:
            while stack and curTime + stack[-1][2] <= work[1]:
                curTime += stack[-1][2]
                answer.append(stack[-1][0])
                stack.pop()
#             if curTime + stack[-1][2] <= work[1]:
                
#                 while stack and curTime + stack[-1][2] < work[1]:
#                     answer.append(stack[-1][0])
#                     curTime += stack[-1][2]
#                     stack.pop()
            if stack:
                stack[-1][2] -= work[1] - curTime
            stack.append(work)
            curTime = work[1]
    if stack:
        while stack:
            answer.append(stack.pop()[0])
    return answer