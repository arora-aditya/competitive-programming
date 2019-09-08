class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # https://leetcode.com/problems/text-justification/
        n = len(words)
        L = maxWidth
        i = 0 
        ans = [] 
        
        def getKwords(i):
            k = 0
            l = ' '.join(words[i:i+k]) 
            while len(l) <= L and i+k <= n:
                k += 1
                l = ' '.join(words[i:i+k])
            k -= 1 
            return k
        
        
        def insertSpace(i, k):
            l = ' '.join(words[i:i+k])       
            if k == 1 or i + k == n:
                spaces = L - len(l)
                line = l + ' ' * spaces 
            else:                           
                spaces = L - len(l) + (k-1)
                space = spaces // (k-1)
                left = spaces % (k-1)
                if left > 0:
                    line = ( " " * (space + 1) ).join(words[i:i+left])
                    line += " " * (space + 1)
                    line += (" " * space).join(words[i+left:i+k])
                else: 
                    line = (" " * space).join(words[i:i+k])
            return line
        

        while i < n: 
            k = getKwords(i)  
            line = insertSpace(i, k)
            ans.append(line) 
            i += k 
        return ans	