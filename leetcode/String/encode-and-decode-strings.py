class Codec:
    # https://leetcode.com/problems/encode-and-decode-strings/
    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return "-."
        return '+&*+'.join(strs)

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        if s == "-.":
            return []
        return s.split('+&*+')


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
["q?6?^7z5*","2_`Gw","+_D4-.3","-z5PU2="]
["q?6?^7z5*","2_`Gw+","_D4-.3","-z5PU2="]
