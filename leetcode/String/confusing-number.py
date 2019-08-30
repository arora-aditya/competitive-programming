class Solution:
    def confusingNumber(self, N: int) -> bool:
       pairs = {
        # '2': '5',
        # '5': '2',
        '1': '1',
        '8': '8',
        '6': '9',
        '9': '6'
       }
       k = ''
       for i in str(N):
           if i in pairs:
               k = k + pairs[i]
           else:
               k = k + i
        return int(k) == N