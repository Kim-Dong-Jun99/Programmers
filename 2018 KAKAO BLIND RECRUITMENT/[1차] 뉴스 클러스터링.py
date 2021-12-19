def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    setStr1 = set()
    setStr2 = set()
    Str1 = []
    Str2 = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            setStr1.add(str1[i:i+2])
            Str1.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            setStr2.add(str2[i:i+2])
            Str2.append(str2[i:i+2])
    if len(setStr1.union(setStr2)) == 0:
        return 65536
    else:
        intersect = 0
        union = 0
        for i in setStr1.intersection(setStr2):
            intersect += min(Str1.count(i),Str2.count(i))
        for i in setStr1.union(setStr2):
            union += max(Str1.count(i),Str2.count(i))
        return int(intersect/union * 65536)