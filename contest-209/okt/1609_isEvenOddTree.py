# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nodes = [root]
        level = 0

        while nodes:
            count = len(nodes)
            evenPrev, oddPrev, oddCheck = -1, -1, 0
            for i in range(count):
                node = nodes.pop(0)
                if (node == None): continue

                if(level % 2 == 0):
                    if(evenPrev < node.val and node.val % 2 == 1):
                        evenPrev = node.val
                    else:
                        return False
                else:
                    if(oddCheck == 0 and node != None):
                        oddPrev = node.val + 1
                        oddCheck = 1

                    if (oddPrev > node.val and node.val % 2 == 0):
                        oddPrev = node.val
                    else:
                        return False

                nodes.append(node.left)
                nodes.append(node.right)
            level += 1

        return True

if __name__=="__main__":
    root = [1,10,4,3, None,7,9,12,8,6,None,None,2]

    sol = Solution()
    result = sol.isEvenOddTree(root)
    print(result)