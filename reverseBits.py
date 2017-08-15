def reverseBits(n):
    """
    https://leetcode.com/problems/reverse-bits/#/description
    """
    n_bin = "{0:b}".format(n)
    n_bin = str(n_bin)
    print(n_bin)
    n_bin = n_bin[::-1] + "0" * (32 - len(n_bin))
    print(n_bin)
    return int(n_bin,2)

print(reverseBits(1))
