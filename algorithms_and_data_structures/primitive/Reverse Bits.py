class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        reverse_binary = str(bin(n))[2:]
        reverse_binary = reverse_binary[::-1]
        missing = 32 - len(reverse_binary)
        reverse_binary = reverse_binary + '0' * missing
        reverse_n = int(reverse_binary, 2)
        return reverse_n

s = 43261596
d = Solution()
print(d.reverseBits(s))