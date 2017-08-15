def longestPalindromeSubseq(s):
    """
    https://leetcode.com/problems/longest-palindromic-subsequence/#/description
    :type s: str
    :rtype: int
    """
    count, max_odd = 0, 0
    char_dict = {}
    for char in s:
        char_dict[char] = char_dict.get(char, 0) + 1
    for char in char_dict:
        if char_dict[char] % 2 == 0:
            count += char_dict[char]
        else:
            max_odd = max(max_odd,char_dict[char])

    return count + max_odd

print(longestPalindromeSubseq("bbbab"))
