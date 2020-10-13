class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        if len(stoneValue) == 1: return 0
        count, result = len(stoneValue) - 2, 0
        while(count != -1):
            left, right = 1, len(stoneValue)-2
            lValue, rValue = stoneValue[0], stoneValue[-1]
            while(count != 0):
                if(lValue-rValue > 0):
                    rValue += stoneValue[right]
                    right -= 1
                    count -= 1
                else:
                    lValue += stoneValue[left]
                    left += 1
                    count -= 1
            if(lValue-rValue > 0):
                stoneValue = stoneValue[right+1:]
                result += sum(stoneValue)
            else:
                stoneValue = stoneValue[:left]
                result += sum(stoneValue)
                # TODO: same length -> choose which Minimum Value
                # using dfs after making values tree
            count = len(stoneValue) - 2

        return result


if __name__=="__main__":
    stoneValue = [2,3,1,4]
    sol = Solution()
    result = sol.stoneGameV(stoneValue)
    print(result)