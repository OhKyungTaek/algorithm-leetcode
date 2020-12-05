class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        import collections
        road = collections.defaultdict(list)
        
        for i in roads:
            road[i[0]].append(i[1])
            road[i[1]].append(i[0])

        result = 0
        for a, b in road.items():
            for r, c in road.items():
                if (a == r): continue
                temp = len(b) + len(c)
                if (a in c): temp -= 1
                result = max(result, temp)

        return result


if __name__ == "__main__":
    n = 8
    roads = [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]

    sol = Solution()
    result = sol.maximalNetworkRank(n, roads)
    print(result)
