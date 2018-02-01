class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] != 9:
            digits[-1] += 1
        else:
            digits[-1] = 0
            carry = 1
            for i in range(len(digits)-2,-1,-1):
                # print(digits)
                su = digits[i]+carry
                carry = su//10
                su = su%10
                digits[i] = su
                if carry == 0:
                    break
                # print(digits)
            if carry != 0:
                digits = [carry] + digits[:]
        # print(digits)
        return digits
