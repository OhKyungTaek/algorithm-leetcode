class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        count = 0
        for i in logs:
            if(i == "../"):
                if(count > 0): count -= 1
            elif( i == "./"):
                continue
            else:
                count += 1

        return count

if __name__=="__main__":
    logs = ["d1/","d2/","../","d21/","./"]

    sol = Solution()
    result = sol.minOperations(logs)
    print(result)