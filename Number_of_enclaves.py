from collections import defaultdict
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        count = defaultdict(int); boolean = defaultdict(lambda: False)
        def dfs(i,j, group):
            nonlocal n; nonlocal m;
            if i<0 or i >= n or j < 0 or j>=m or grid[i][j] == 0:
                return
            count[group] +=1
            grid[i][j] = 0
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                boolean[group] = True
            dfs(i, j+1, group); dfs(i, j-1, group); dfs(i+1, j, group); dfs(i-1,j, group)
        group_num = 0
        for in_x in range(n):
            for in_y in range(m):
                if grid[in_x][in_y] == 1:
                    dfs(in_x, in_y, group_num)
                    group_num += 1
        answer = 0
        for z in count:
            if not boolean[z]:
                answer += count[z]
        return answer
                    

