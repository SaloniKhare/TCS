import heapq

class Solution:
    def mergeArrays(self, mat):
        h = []
        n = len(mat)
        m = len(mat[0])
        for i in range(n):
            heapq.heappush(h, (mat[i][0], i, 0))
            
        ans = []
        while h:
            val, r, c = heapq.heappop(h)
            ans.append(val)
            if c + 1 < m:
                heapq.heappush(h, (mat[r][c + 1], r, c + 1))
                
        return ans
