class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        sortedPiles = sorted(piles)
        sum, i, j = 0, 0, len(piles)-2
        while i < j:
            i += 1
            sum += sortedPiles[j]
            j -= 2

        return sum

# Slow version
# for i in range(len(piles)//3):
#     sortedPiles.pop(0)
#     sortedPiles.pop(-1)
#     sum += sortedPiles.pop(-1)


if __name__=="__main__":
    piles = [2,4,1,2,7,8]
    sol = Solution()
    result = sol.maxCoins(piles)
    print(result)