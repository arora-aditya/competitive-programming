class Solution:
    def defangIPaddr(self, address: str) -> str:
        # https://leetcode.com/problems/defanging-an-ip-address/
        return address.replace('.','[.]')