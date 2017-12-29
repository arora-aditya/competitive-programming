nim_dict={1:True,2:True,3:True,4:False}
def canWinNim(n):
    """
    https://leetcode.com/problems/nim-game/#/description
    :type n: int
    :rtype: bool
    """
    global nim_dict
    if n in nim_dict:
        return nim_dict[n]
    if canWinNim(n-1) == False or canWinNim(n-2)==False or canWinNim(n-3)==False:
        nim_dict[n]=True
        return True
    nim_dict[n]=False
    return False

print(nim_dict)
print(canWinNim(8))
