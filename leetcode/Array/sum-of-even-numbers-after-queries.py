class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        su0 = sum([a for a in A if a % 2 == 0])
        ans = []

        for query in queries:
            val = query[0]
            index = query[1]
            prev = A[index]
            A[index] += val

            if A[index] % 2 == 0:
                if prev % 2 ==0:
                    su0 += val
                else:
                    su0 += A[index]
            else:
                if prev % 2 == 0:
                    su0 -= prev

            ans.append(su0)

        return ans
