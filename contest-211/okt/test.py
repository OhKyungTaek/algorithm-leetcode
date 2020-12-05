# class Solution(object):
#     def bestTeamScore(self, scores, ages):
#         """
#         :type scores: List[int]
#         :type ages: List[int]
#         :rtype: int
#         """
#         length = len(scores)
#         players = [[ages[i], scores[i]] for i in range(length)]
#         players = sorted(players)
#         score = [players[i][1] for i in range(length)]
#
#         cumulative = [-1] * length
#         cumulative[0] = score[0]
#
#         for i in range(1, length):
#             cumulative[i] = score[i]
#             for j in range(0, i):
#                 if (score[i] >= score[j]):
#                     cumulative[i] = max(cumulative[i], cumulative[j] + score[i])
#
#         return max(cumulative)

class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """

        max_scores = [0] * (max(ages) + 1)
        for score, age in sorted(zip(scores, ages)):
            max_scores[age] = score + max(max_scores[:age + 1])

        return max(max_scores)


if __name__ == "__main__":
    scores = [1, 4, 6, 8, 3, 5, 6, 7]
    ages = [1, 2, 3, 4, 5, 6, 7, 8]

    sol = Solution()
    result = sol.bestTeamScore(scores, ages)
    print(result)
