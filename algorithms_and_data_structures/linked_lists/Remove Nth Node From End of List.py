# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        linked_list = []
        current = head
        while current != None:
            linked_list.append(current)
            current = current.next
        if n == len(linked_list):
            head = head.next
        elif n == 1:
            last = linked_list[-2]
            last.next = None
        else:
            previous = linked_list[-(n + 1)]
            next_node = linked_list[-(n - 1)]
            previous.next = next_node
        return head

s = 3
d = Solution()
print(d.countAndSay(s))