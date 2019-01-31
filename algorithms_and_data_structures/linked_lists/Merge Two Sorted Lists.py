class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            root = l1
            l1 = l1.next
        else:
            root = l2
            l2 = l2.next
        current = root
        list1 = l1
        list2 = l2
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                current = current.next
                list1 = list1.next
            else:
                current.next = list2
                current = current.next
                list2 = list2.next
        if list1:
            current.next = list1
        else:
            current.next = list2
        return root
                
time = [[1,2,4],[1,3,4]]
time2 = []
for i in time:
    root = ListNode(i[0])
    current = root
    for j in range(len(i) - 1):
        current.next = ListNode(i[j+1])
        current = current.next
    time2.append(root)

time3 = [[]]
d = Solution()
print(d.mergeTwoLists(time2[0],time2[1]))
