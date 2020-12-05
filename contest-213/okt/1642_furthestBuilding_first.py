class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        for i in range(len(heights)-1):
            if heights[i] > heights[i+1]:
                continue
            diff = heights[i + 1] - heights[i]
            if diff <= bricks:
                bricks -= diff
                continue

            elif ladders > 0:
                ladders -= 1
                continue

            return i
        return len(heights) - 1

if __name__ == '__main__':
    heights = [4,12,2,7,3,18,20,3,19]
    bricks = 10
    ladders = 2

    sol = Solution()
    result = sol.furthestBuilding(heights, bricks, ladders)
    print(result)