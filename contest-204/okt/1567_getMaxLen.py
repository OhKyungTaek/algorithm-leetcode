class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev, curr = [0, 0], [0, 0]
        maxlen = 0

        for i in nums:
            curr[:] = prev[:]
            if(i > 0):
                prev[0] = curr[0] + 1
                if(curr[1] != 0):
                    prev[1] = curr[1] + 1
            elif(i < 0):
                prev[1] = curr[0] + 1
                if (curr[1] != 0):
                    prev[0] = curr[1] + 1
                else:
                    prev[0] = 0
            maxlen = max(maxlen, prev[0])
            if(i == 0):
                prev = [0, 0]
        return maxlen

if __name__=="__main__":
    nums = [1,2,3,5,-6,4,0,10]
    sol = Solution()
    result = sol.getMaxLen(nums)
    print(result)

# learned
# shallow : arr1 = arr2, arr1 = arr2[:]
# deep : arr1[:] = arr2[:]