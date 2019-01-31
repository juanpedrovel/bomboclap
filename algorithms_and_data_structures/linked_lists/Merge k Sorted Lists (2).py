class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return
        lens = len(lists)
        result = None
        changes = 1
        root = None
        while True:
            changes = 0
            mini = float('inf')
            index = None
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if lists[i].val <= mini:
                    mini = lists[i].val
                    index = i
                    changes += 1
            if changes == 0:
                break
            if not result:
                result = lists[index]
                root = result
            else:
                result.next = lists[index]
                result = result.next
            lists[index] = lists[index].next
            result.next = None
        if root == None:
            return lists
        return root
                
time = [[1,4,5],[1,3,4],[2,6]]
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
print(d.mergeKLists(time3))
