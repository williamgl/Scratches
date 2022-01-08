# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        answer = []
        level = [root]
        count = 1
        temp = []

        while level:

            for node in level:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            if count % 2 == 0:
                level.reverse()

            answer.append(node.val for node in level)

            level = temp
            temp = []

            count += 1

        return answer