class Solution(object):
    def mostVisited(self, n, rounds):
        """
        :type n: int
        :type rounds: List[int]
        :rtype: List[int]
        """
        queue = []
        if(rounds[0] <= rounds[-1]):
            for i in range(rounds[0], rounds[-1]+1):
                queue.append(i)
        else:
            for i in range(1, n+1):
                if(rounds[0] <= i or rounds[-1] >= i):
                    queue.append(i)

        return queue


if __name__=="__main__":
    n = 3
    rounds = [3, 2, 1, 2, 1, 3, 2, 1, 2, 1, 3, 2, 3, 1]
    sol = Solution()
    result = sol.mostVisited(n, rounds)
    print(result)