class Solution:
    def myAtoi(self, str: str) -> int:
        # https://leetcode.com/problems/string-to-integer-atoi
        def isNumber(s):
            numbers = s.split(' ')
            numbers = list(filter(None, numbers))
            if len(numbers) != 0 and len(numbers)<=1:
                for num in numbers:
                    try:
                        float(num)
                    except:
                        return False
                return True
            else:
                return False

        if len(str) != 0 and str not in '+-' and '+-' not in str:
            numbers=str.split(' ')
            numbers = list(filter(None, numbers))
            if len(numbers) > 0:
                num=numbers[0]
                num=(num.split('e'))[0]
                # print(type(num))
                for i in range(len(num),0,-1):
                    if isNumber(num[0:i]):
                        num=num[0:i]
                        if float(num) < -2147483648:
                            return -2147483648
                        elif float(num) > 2147483647:
                            return 2147483647
                        if '.' in num:
                            return int(float(num))
                        return int(num)
            return 0
        else:
            return 0