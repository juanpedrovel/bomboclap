class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        final_list = None
        while not final_list:
            if not lists:
                return
            final_list = lists.pop()
        root = final_list
        for i in range(len(lists)):
            current = lists[i]
            while current != None:
                if current.val <= root.val:
                    lists[i] = current.next
                    current.next = root
                    root = current
                else:
                    position = root
                    while position.next != None:
                        if current.val < position.next.val:
                            break
                        position = position.next
                    lists[i] = current.next
                    current.next = position.next
                    position.next = current
                current = lists[i]
        return root
                
time = [[1,2,3],[4,5,6,7]]
time2 = []
for i in time:
    root = ListNode(i[0])
    current = root
    for j in range(len(i) - 1):
        current.next = ListNode(i[j+1])
        current = current.next
    time2.append(root)


d = Solution()
print(d.mergeKLists(time2))
