class Node():
    def __init__(self, data):
        self.data = data
        self.child = {}
        self.childNum = 0


class Trie():
    def __init__(self):
        self.head = Node(None)

    def insert(self, data):
        itr = self.head
        for i in data:
            if (i in itr.child) == False:
                itr.child[i] = Node(i)
            itr = itr.child[i]
            itr.childNum += 1

    def search(self, query):
        nextNode = [self.head]
        # print(self.head.child)
        result = 0
        # print(query)
        for i in query:
            if i != 'and':
                if i == '-':
                    temp = []
                    for j in nextNode:
                        for k in j.child:
                            temp.append(j.child[k])
                    nextNode = temp
                else:
                    if i[0].isdigit():
                        # print(1)
                        temp = []
                        for j in nextNode:
                            for k in j.child:
                                if int(j.child[k].data) >= int(i):
                                    result += j.child[k].childNum
                        return result
                    else:
                        # print(i)
                        temp = []
                        for j in nextNode:
                            if (i in j.child):
                                temp.append(j.child[i])
                        if temp == []:
                            return 0
                        nextNode = temp


def solution(info, query):
    answer = []
    trie = Trie()
    for i in info:
        temp = i.split()
        trie.insert(temp)
    for i in query:
        temp = i.split()
        answer.append(trie.search(temp))

    return answer