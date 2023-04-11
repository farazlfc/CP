from collections import defaultdict
class Solution:
    def dfs(self, x, y, scalar):
        self.seen.add(x)
        for new, val in self.adj[x]:
            if new == y:
                return scalar*val
            if new not in self.seen:
                cal = self.dfs(new, y, scalar*val)
                if cal!= -1:
                    return cal
        return -1


    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.seen = set()
        n = len(equations)
        self.adj = defaultdict(list)
        for i in range(n):
            x, y, value = equations[i][0], equations[i][1], values[i]
            self.adj[x].append((y, value))
            self.adj[y].append((x, 1.0/value))
        answer = []
        for x, y in queries:
            if x not in self.adj or y not in self.adj:
                answer.append(-1)
            else:
                self.seen = set()
                val = self.dfs(x, y, 1)
                answer.append(val)
        return answer

