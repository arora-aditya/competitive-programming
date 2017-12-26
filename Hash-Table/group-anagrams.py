def groupAnagrams(strs):
    """
    https://leetcode.com/problems/group-anagrams/#/solutions
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    d = {}
    for w in sorted(strs):
        key = tuple(sorted(w))
        d[key] = d.get(key, []) + [w]
    return d.values()
