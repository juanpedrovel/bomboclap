class Node:
    def __init__(self, index):
        self.index = index
        self.next = None

class Solution:
    def repeatedStringMatch(self, A, B):
        chars_A = [False] * 26
        for i in A:
            x = ord(i) - 97
            chars_A[x] = True
        for i in B:
            y = ord(i) - 97
            if chars_A[y] == False:
                return -1
        positions = []
        for i in range(len(A)):
            if A[i] == B[0]:
                positions.append(i)
        if not positions:
            return -1
        good = False
        for k in positions:
            good = True
            repetitions = 1
            for j in range(len(B)):
                if B[j] != A[(k + j) % len(A)]:
                    k += 1
                    good = False
                    break
                if (k + j) % len(A) == 0:
                    repetitions += 1
                    if k + j == 0:
                        repetitions -= 1
            current = None
        if good == True:
            return repetitions
        else:
            return -1

A = "abcd"
B = "cdabcdab"
d = Solution()
print(d.repeatedStringMatch(A, B))