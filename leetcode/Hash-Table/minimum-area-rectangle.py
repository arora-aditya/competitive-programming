lass Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # https://leetcode.com/problems/minimum-area-rectangle/
        x,y={},{}
        minArea = float('inf')
        for point in points:
            # print(x,y)
            setX = x.get(point[0], set())
            setX.add(point[1])
            x[point[0]] = setX
            setY = y.get(point[1], set())
            setY.add(point[0])
            y[point[1]] = setY
        # print(x)
        # print(y)
        XC = list(sorted(x.keys()))
        for i in range(len(XC)):
            for j in range(i+1, len(XC)):
                if abs(XC[i] - XC[j]) < minArea and len(x[XC[i]]) > 1 and len(x[XC[j]]) > 1:
                    for y1 in x[XC[i]]:
                        if y1 in x[XC[j]]:
                            for y2 in x[XC[j]]:
                                if len(y[y1]) > 1 and len(y[y2]) > 1 and y1 != y2 and y2 in x[XC[i]]:
                                    area = abs(XC[i] - XC[j]) * abs(y1-y2)
                                    if area < minArea:
                                        print(XC[i], XC[j], y1, y2, minArea, area)
                                        minArea = area
                # yS = []
                # for y1 in x[XC[i]]:
                #     print(XC[i], XC[i-1], y[y1])
                #     if XC[i] in y[y1] and XC[i-1] in y[y1]:
                #         yS.append(y1)
                # print(yS)
                # if len(yS) >= 2:
                #     for y1 in yS:
                #         for y2 in yS:
                #             minArea = min(minArea, abs(XC[i] - XC[i-1]) * abs(y1-y2))
        return 0 if minArea == float('inf') else minArea
