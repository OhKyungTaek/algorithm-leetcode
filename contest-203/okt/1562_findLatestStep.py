class Solution(object):
    def findLatestStep(self, arr, m):
        """
        :type arr: List[int]
        :type m: int
        :rtype: int
        """
        length = len(arr)
        if length == m : return m
        diction = list()
        diction.append([0, length])
        for i in range(length-1, -1, -1):
            target = arr[i]
            place = self.findSliceSpace(diction, target)

            left = target - diction[place][0] - 1
            right = diction[place][1] - (target - diction[place][0])

            if(left == m or right == m):
                return i
            else:
                diction[place][1] = left
                diction.insert(place + 1, [target, right])
        return -1

    def findSliceSpace(self, list, target):
        le = len(list)
        for i in range(len(list)):
            if(list[i][0] > target):
                return i-1
        return le-1



if __name__=="__main__":
    arr = [4,3,2,1]
    m = 1
    sol = Solution()
    result = sol.findLatestStep(arr, m)
    print(result)