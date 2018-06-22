class Solution:
    def IPv4(self, IP):
        IP = IP.split('.')
        if len(IP) != 4:
            return False
        try:
            for i in IP:
                if len(i) == 0 or len(i) > 3:
                    return False
                elif i > '255' or i < '0':
                    return False
                if str(int(i)) != i:
                    return False
            return True
        except:
            return False
    def IPv6(self, IP):
        IP = IP.split(':')
        if len(IP) != 8:
            return False
        for i in IP:
            if len(i) == 0 or len(i) > 4:
                return False
            for j in i:
                if (j > 'f' or j < 'a') and (j > 'F' or j < 'A') and (j < '0' or j > '9'):
                    return False
        return True

    def validIPAddress(self, IP):
        """
        https://leetcode.com/problems/validate-ip-address/description/
        :type IP: str
        :rtype: str
        """
        if self.IPv4(IP):
            return "IPv4"
        if self.IPv6(IP):
            return "IPv6"
        return "Neither"
