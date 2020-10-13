class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        for i in range(0, len(arr)-m*k+1):
            sub = arr[i:i+m]
            if(sub*k == arr[i:i+m*k]):
                return True
        return False


if __name__=="__main__":
    arr = [2,2]
    m = 1
    k = 2
    sol = Solution()
    result = sol.containsPattern(arr, m, k)
    print(result)

# learned : arr * 3 -> arr arr arr