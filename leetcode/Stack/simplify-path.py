class Solution:
    def simplifyPath(self, path: str) -> str:
        # https://leetcode.com/problems/simplify-path
        st = path.split('/')
        # print(st)
        st_new = []
        for subpath in st:
            # print(subpath, subpath == '')
            if subpath == '' or subpath == '.':
                pass
            elif subpath == '..':
                if len(st_new) > 0:
                    st_new.pop()
            else:
                st_new.append(subpath)
        # print(st_new)
        return '/'+'/'.join(st_new)
        
        