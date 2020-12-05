class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        res = [0, 1]
        for i in range(2, n + 1):
            if i % 2 == 0:
                res.append(res[i // 2])
            else:
                res.append(res[i // 2] + res[i // 2 + 1])
        return max(res)


if __name__ == '__main__':
    n = 4

    sol = Solution()
    result = sol.getMaximumGenerated(n)
    print(result)