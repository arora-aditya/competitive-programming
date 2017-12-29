def maxPoints(self, points):
    """
    https://leetcode.com/problems/max-points-on-a-line/description/
    :type points: List[Point]
    :rtype: int
    """
    l = len(points)
    if l == 0:
        return 0
    if l == 1:
        return 1
    m = 0
    for i in range(l):
        dic = {'i': 1}
        same = 0
        for j in range(i+1, l):
            tx, ty = points[j].x, points[j].y
            if tx == points[i].x and ty == points[i].y: 
                same += 1
                continue
            if points[i].x == tx: slope = 'i'
            else:slope = ((points[i].y-ty) * np.longdouble(1)) /(points[i].x-tx)
            if slope not in dic: dic[slope] = 1
            dic[slope] += 1
        m = max(m, max(dic.values()) + same)
    return m
