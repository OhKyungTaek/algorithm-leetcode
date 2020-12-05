class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        length = len(scores)
        players = [[ages[i], scores[i]] for i in range(length)]
        players = sorted(players)
        score = [players[i][1] for i in range(length)]

        remember = [-1] * length
        remember[0] = score[0]

        for i in range(1, length):
            remember[i] = score[i]
            for j in range(0, i):
                if (score[i] >= score[j]):
                    remember[i] = max(remember[i], score[i] + remember[j])

        return max(remember)


if __name__ == "__main__":
    scores = [4, 5, 6, 5]
    ages = [2, 1, 2, 1]

    sol = Solution()
    result = sol.bestTeamScore(scores, ages)
    print(result)