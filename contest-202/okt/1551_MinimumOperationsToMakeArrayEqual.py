class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n % 2 == 1):
            return (n//2) * ((n//2) + 1)
        else:
            return (n//2)**2
        # return (n//2) * round((n / 2) + 0.1)

if __name__=="__main__":
    arr = 3

    sol = Solution()
    result = sol.minOperations(arr)
    print(result)