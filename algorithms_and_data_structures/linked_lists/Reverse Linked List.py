# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        linked_list = []
        if not head:
            return
        current = head
        while current != None:
            linked_list.append(current)
            current = current.next
        for i in range(len(linked_list)-1, 0, -1):
            linked_list[i].next = linked_list[i-1]
        linked_list[0].next = None
        head = linked_list[-1]
        return head

s = "aaabbcc"
dict = ["aaa","aab","bc"]
d = Solution()
print(d.addBoldTag(s, dict))