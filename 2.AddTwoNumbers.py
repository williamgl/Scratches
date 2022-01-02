class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        zero = ListNode()

        answer.val += l1.val + l2.val

        if l1.next is None and l2.next is None:
            if answer.val >= 10:
                answer.next = zero
        elif l2.next is None:
            answer.next = self.addTwoNumbers(l1.next, zero)
        elif l1.next is None:
            answer.next = self.addTwoNumbers(zero, l2.next)
        else:
            answer.next = self.addTwoNumbers(l1.next, l2.next)
        self.checkAndChange(answer)

        return answer

    def checkAndChange(self, node):
        one = ListNode(1)
        if node.val >= 10:
            node.val -= 10
            if node.next is None:
                node.next = one
                return
            else:
                node.next.val += 1
                self.checkAndChange(node.next)