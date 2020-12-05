class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        result = [True] * len(l)
        for i in range(len(l)):
            subarr = nums[l[i]:r[i] + 1]
            subarr = sorted(subarr)
            prev = 0
            for j in range(len(subarr) - 1):
                ele1 = subarr[j]
                ele2 = subarr[j + 1]
                if (j == 0):
                    prev = ele2 - ele1
                    continue
                else:
                    temp = ele2 - ele1
                    if (prev != temp):
                        result[i] = False
                        break
                prev = temp
        return result


if __name__ == '__main__':
    nums = [-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10]
    l = [0, 1, 6, 4, 8, 7]
    r = [4, 4, 9, 7, 9, 10]

    sol = Solution()
    result = sol.checkArithmeticSubarrays(nums, l, r)
    print(result)
