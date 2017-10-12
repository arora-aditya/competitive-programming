class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        print(hex(num))
        st = ""
        base16 = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
        if num > 0:
            while num > 0:
                st += base16[num%16]
                num //= 16
            return st[::-1]
        elif num == 0:
            return "0"
        else:
            base16 = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"][::-1]
            
            num = num*(-1)
            while num > 0:
                st += base16[num%16]
                num //= 16
            add_digit = {"0":"1","1":"2","2":"3","3":"4","4":"5","5":"6","6":"7","7":"8","8":"9","9":"a","a":"b","b":"c","c":"d","d":"e","e":"f","f":"0"}
            st = st[::-1]
            if(len(st) < 8):
                st = (8-len(st))*"f" + st
            return st[:-1]+add_digit[st[-1]]
                
        
