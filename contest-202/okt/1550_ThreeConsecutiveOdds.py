class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        check = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 1:
                check += 1
            else:
                check = 0
            if(check == 3):
                return True

        return False



if __name__=="__main__":
    arr = [2, 6, 4, 1]

    sol = Solution()
    result = sol.threeConsecutiveOdds()
    print(result)