class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        spaces = text.count(' ')
        words = text.split()
        result = ''
        check = False

        if(len(words) == 1):
            return words[0] + (' ' * spaces)
        for i in range(len(words)):
            result += words[i]
            if(i != len(words)-1):
                result += ' ' * (spaces // (len(words) - 1))

        if(len(words) <= 1):
            result += ' ' * spaces
        else:
            result += ' ' * (spaces % (len(words) - 1))

        return result


if __name__=="__main__":
    text = "a"

    sol = Solution()
    result = sol.reorderSpaces(text)
    print(result)