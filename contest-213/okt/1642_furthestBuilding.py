from heapq import *
class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        heap = []

        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]

            if(diff > 0):
                heappush(heap, diff)
            if(len(heap) > ladders):
                bricks -= heappop(heap)
            if(bricks < 0):
                return i
        return len(heights) - 1

if __name__ == '__main__':
    heights = [4, 12, 2, 7, 3, 18, 20, 3, 19]
    bricks = 10
    ladders = 2

    sol = Solution()
    result = sol.furthestBuilding(heights, bricks, ladders)
    print(result)
