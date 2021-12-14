def solution(lottos, win_nums):
    common = 0

    for i in win_nums:
        if (i in lottos):
            common += 1
    if common == 0:
        worstRank = 6
        if lottos.count(0) == 0:
            bestRank = 6
        else:
            bestRank = 7 - lottos.count(0)
    else:
        worstRank = 7 - common
        bestRank = 7 - common - lottos.count(0)

    answer = [bestRank, worstRank]
    return answer