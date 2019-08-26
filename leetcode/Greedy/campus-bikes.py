class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        def dist(x, y):
            mi = float('inf')
            b = None
            
            for i, (b_x, b_y) in bikes.items():
                d = abs(x - b_x) + abs(y - b_y)
                
                if d < mi:
                    mi = d
                    b = i
                    
            return mi, b
        
        bikes = dict(enumerate(bikes))
        seen = set()
        ans = [None] * len(workers)
        q = []
        
        for j, (x, y) in enumerate(workers):
            d, i = dist(x, y)
            heapq.heappush(q, (d, j, i))
            
        while len(seen) < len(workers):
            _, j, i = heapq.heappop(q)
            
            if i in seen:
                x, y = workers[j]
                d, i = dist(x, y)
                heapq.heappush(q, (d, j, i))
                
            else:
                ans[j] = i
                seen.add(i)
                del bikes[i]
                
        return ans
        
    def assignBikesSlower(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        # https://leetcode.com/problems/campus-bikes/
        def dist(w, b):
            return abs(w[1] - b[1]) + abs(w[0] - b[0])
        ds = []
        for j, w in enumerate(workers):
            ds.append([])
            for i, b in enumerate(bikes):
                ds[-1].append([dist(w, b), j, i])
            ds[-1].sort(reverse = True)
        q = [x.pop() for x in ds]
        heapq.heapify(q)
        used_bikes = set()
        ans = [None]*len(workers)

        while len(used_bikes) < len(workers):
            d, j, i = heapq.heappop(q)
            if i not in used_bikes:
                used_bikes.add(i)
                ans[j] = i
            else:
                heapq.heappush(q, ds[j].pop())
        return ans