class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        returnArray = []

        def depthFirstSearch(k: int):

            if k > n:
                return

            returnArray.append(k)

            for i in range(10):
                nextNum = 10 * k + i
                if nextNum > n:
                    return
                else:
                    depthFirstSearch(nextNum)

        for i in range(1, 10):
            if i > n:
                break
            else:
                depthFirstSearch(i)

        return returnArray