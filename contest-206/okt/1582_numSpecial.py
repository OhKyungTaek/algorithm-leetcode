class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        rowDict = dict()
        colDict = dict()
        h, w = len(mat), len(mat[0])

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if(mat[row][col] == 1):
                    rowDict[row] += 1
                    colDict[col] += 1

        sum = 0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if(mat[row][col]) and (1 == rowDict[row]) and (1 == colDict[col]):
                    sum += 1

        return sum

if __name__=="__main__":
    mat = [[1, 0, 0],
           [0, 0, 1],
           [1, 0, 0]]
    sol = Solution()
    result = sol.numSpecial(mat)
    print(result)