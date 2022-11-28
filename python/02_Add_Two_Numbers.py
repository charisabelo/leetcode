# time - o(n)
# space - O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        c1 = ''
        c2 = ''

        while curr1 != None or curr2 != None:
            if curr1 != None:
                c1 += str(curr1.val)
                curr1 = curr1.next

            if curr2 != None:
                c2 += str(curr2.val)
                curr2 = curr2.next

        m = int(c1[::-1]) + int(c2[::-1])
        n = str(m)[::-1]
        print(m, c1, c2)

        output = None
        curr = None

        for num in n:

            if output == None:
                output = ListNode(int(num), None)
                curr = output
            else:
                new_node = ListNode(int(num), None)
                curr.next = new_node
                curr = curr.next

        return output
