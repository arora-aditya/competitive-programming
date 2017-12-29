def lengthOfLongestSubstring(s):
    """
    https://leetcode.com/problems/longest-substring-without-repeating-characters/#/description
    :type s: str
    :rtype: int
    """
    if len(s)==0:
        return ""
    else:
        def isrepeat(s):
            s=sorted(s)
            char_list=[]
            for char in s:
                if char in char_list:
                    return False
                else:
                    char_list.append(char)
            return True
        max_len=0
        saved_string=s[0]
        for i in range(len(s)+1):
            for j in range(len(s),-1,-1):
                print(s[i:j],isrepeat(s[i:j]),saved_string,max_len)
                if max_len<(j-i):
                    if isrepeat(s[i:j]):
                        max_len=j-i
                        saved_string=s[i:j]
                else:
                    break
        return saved_string
