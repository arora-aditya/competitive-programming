def isInterleave(s1, s2, s3):
    """
    https://leetcode.com/problems/interleaving-string/description/
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """
    k,i,j=0,0,0
    char=s3[k]
    if len(s3)!=len(s1)+len(s2):
        return False
    while k < len(s3):
        flag=True
        while i < len(s1) and k < len(s3) and s3[k] == s1[i]:
            char=s3[k]
            i += 1
            k += 1
            flag=False
        while j < len(s2) and k < len(s3) and s3[k] == s2[j]:
            char=s3[k]
            j += 1
            k += 1
            flag=False
        if flag:
            char=s3[k]
            k += 1
        else:
            break

    if i != len(s1) or j!= len(s2):
        return False
    return True
