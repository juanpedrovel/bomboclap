class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lens = len(s)
        self.counter = 0
        rows = []
        for i in range(numRows):
            rows.append([])
            
        def zig():
            for i in range(numRows):
                if self.counter == lens:
                    break
                rows[i].append(s[self.counter])
                self.counter += 1
        
        def zag():
            for i in range(numRows - 2, 0, -1):
                if self.counter == lens:
                    break
                rows[i].append(s[self.counter])
                self.counter += 1
        
        while self.counter < lens:
            zig()
            zag()
        
        for i in range(numRows):
            rows[i] = ''.join(rows[i])
            
        return ''.join(rows)