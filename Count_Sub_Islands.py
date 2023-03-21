from collections import defaultdict
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        #if int then change to boolea
        #traverse and mark common cells with # 
        n,m = len(grid1), len(grid1[0])
        def dfs(x,y, group):
            if x < 0 or x >= n or y < 0 or y >= m or grid2[x][y] == 0:
                return
            if grid1[x][y] == 0:
                boolean[group] = False
            count[group] += 1
            grid2[x][y] = 0
            pots = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            for (a,b) in pots:
                dfs(a, b, group)
        boolean = defaultdict(lambda: True)
        count = defaultdict(int)
        group = 0
        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1:
                    dfs(i, j, group)
                    group += 1
        answer = 0
        #print(count, boolean)
        for k in count:
            if boolean[k]:
                answer += 1
        
        return answer
