class Graph:
  def __init__(self,v):
    self.v = v
    self.edges = [[] for _ in range(v)]
    self.cc_count = [[] for _ in range(v)]  #[[]]
    self.edge_count = [0]*v
    self.visited = [False]*v
    self.ccs= 0
  def addEdge(self,x,y):
    self.edges[x].append(y)
    self.edges[y].append(x);
  def dfs(self,node,cc_index):
    self.visited[node] = True;
    self.cc_count[cc_index].append(node)
    print(cc_index)
    for k in self.edges[node]:
      if not self.visited[k]:
        self.dfs(k,cc_index)

      
        
  def numberofCCs(self):
    #visited = [False]*self.v
    for i in range(self.v):
      if not self.visited[i]:
        self.ccs+=1
        self.dfs(i,self.ccs-1)
  def get_spare_edges(self):
    spare = 0;
    for i in range(self.ccs):
      length = 0;
      nodes = len(self.cc_count[i])
      for node in self.cc_count[i]:
        length+= len(self.edges[node])
      length = length//2
      spare+= length - (nodes - 1)
    return spare


g = Graph(5); 
g.addEdge(1, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 4)
g.addEdge(4, 2)
g.numberofCCs()
print(g.cc_count)
print(g.ccs)
print(g.get_spare_edges())
