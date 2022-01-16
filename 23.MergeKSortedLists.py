# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(left, right):
            temp = ListNode()
            ans = temp
            while left and right:
                if left.val < right.val:
                    temp.next = left
                    left = left.next
                else:
                    temp.next = right
                    right = right.next
                temp = temp.next
            # when one is none, temp.next are the rest of the other one
            temp.next = left or right
            return ans.next

        if not lists: return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2

        left, right = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return merge(left, right)
