class Codec:
    def __init__(self):
        self.indicator = "#123#123#"

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        encoded = "".join(s + self.indicator for s in strs)
        return encoded

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        strings = s.split(self.indicator)[:-1]
        return strings

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
