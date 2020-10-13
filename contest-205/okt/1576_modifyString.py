class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # left, right, n
        count = 0
        for i in range(len(s)):
            if(ord(s[i]) == 63):
                count += 1
            elif(ord(s[i]) != 63 and count > 0):
                if(i == 0):
                    left = 97
                else:
                    left = ord(s[i-count-1])
                if(i == len(s)):
                    right = 123
                else:
                    right = ord(s[i])
                subs = self.select(left, right, count)
                s = s.replace('?'*count, subs, 1)
                count = 0
        if(count > 0):
            if (i == 0):
                left = 97
            else:
                left = ord(s[i - count])
            if (i == len(s)):
                right = 123
            else:
                right = ord(s[i])
            subs = self.select(left, right, count)
            s = s.replace('?' * count, subs, 1)
            count = 0
        return s

    def select(self, left, right, n):
        temp = []
        count = n
        length = n
        while(length > 0):
            for i in range(97, 123):
                if(i != left and i != right):
                    temp.append(chr(i))
                    count -= 1
                    length -= 1
                if(count == 0 or length == 0):
                    break

        return ''.join(temp)



if __name__=="__main__":
    s = "????????????????????????????????????????????????????????????????????????????????????????????????????"
    sol = Solution()
    result = sol.modifyString(s)
    print(result)