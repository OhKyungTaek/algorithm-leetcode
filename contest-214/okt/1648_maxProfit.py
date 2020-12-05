class Solution(object):
    def maxProfit(self, inventory, orders):
        """
        :type inventory: List[int]
        :type orders: int
        :rtype: int
        """
        items = sorted(inventory, reverse=True)
        length = len(items)
        result, i = 0, 0
        while orders:
            curr = items[i]
            # one element
            if (length == 1):
                return (orders * (curr + curr - orders + 1) // 2) % (10 ** 9 + 7)
            if (i == length - 1):
                next = items[i] - orders + 1
            else:
                next = items[i + 1] + 1
            count = (i + 1) * (curr - next + 1)
            if (count < orders):
                result += (i + 1) * (curr - next + 1) * (curr + next) // 2
                orders -= count
                i += 1
            else:
                number, other = divmod(orders, (i + 1))
                result += (i + 1) * number * (items[i] + (items[i] - number + 1)) // 2
                result += other * (items[i] - number)

                return result % (10 ** 9 + 7)


if __name__ == '__main__':
    inventory =[2,8,4,10,6]
    orders = 20

    sol = Solution()
    result = sol.maxProfit(inventory, orders)
    print(result)
