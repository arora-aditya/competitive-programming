class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx > 0 and ty > 0 and tx != ty and (tx > sx or ty > sy):
            if tx > ty:
                k = (tx - sx) // ty
                tx -= k*ty
            else:
                k = (ty - sy) // tx
                ty -= k*tx
            if k < 1:
                return False
        
        if tx == sx and ty == sy:
            return True
        if tx == ty and ((sx == 0 and sy == tx) or (sy == 0 and sx == tx)):
            return True
        return False