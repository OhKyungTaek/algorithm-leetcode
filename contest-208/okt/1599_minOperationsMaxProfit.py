class Solution(object):
    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        """
        :type customers: List[int]
        :type boardingCost: int
        :type runningCost: int
        :rtype: int
        """
        wait, board= 0, 0
        profit, highest = 0, 0
        rotate, hi_rotate = 0, -1

        for i in customers:
            wait += i
            board = min(4, wait)
            profit += board * boardingCost - runningCost
            wait -= board
            rotate += 1
            if(profit > highest):
                highest = profit
                hi_rotate = rotate

        while(wait != 0):
            board = min(4, wait)
            profit += board * boardingCost - runningCost
            wait -= board
            rotate += 1
            if (profit > highest):
                highest = profit
                hi_rotate = rotate
        if(highest < 0): hi_rotate = -1

        return hi_rotate


if __name__=="__main__":
    customers = [3,4,0,5,1]
    boardingCost = 1
    runningCost = 92

    sol = Solution()
    result = sol.minOperationsMaxProfit(customers, boardingCost, runningCost)
    print(result)