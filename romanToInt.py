def romanToInt(s):
    """
    https://leetcode.com/problems/roman-to-integer/#/description
    :type s: str
    :rtype: int
    """
    roman_list = "IVXLCDM"
    roman_dict={'I':1,"IV":4, "V":5, "IX":9, "X":10, "XL":40, "L":50, "XC":90, "C":100, "CD":400, "D":500, "DM":900, "M":1000}
    i=0
    num=0
    while i < len(s):
        try:
            if roman_list.index(s[i]) < roman_list.index(s[i+1]):
                num += roman_dict[s[i]+s[i+1]]                
                i += 2
            else:
                num += roman_dict[s[i]]
                i += 1
        except IndexError:
            num += roman_dict[s[i]]
            i += 1
    return num

print(romanToInt("MMCXXIV"))
