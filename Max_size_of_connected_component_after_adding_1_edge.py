#CODENATION TEST -> Given a DIRECTED graph, tell the size of the largest Strngly Connected Component you can produce given that you can at max add only one edge?
#LOGIC, Find sizes of all SCCs, and the SCC to which each node belongs. Then if an edge already exists between two nodes of different SCCs, we can create a back edge. Hence, NEW SCC Size => SCC_1 + SCC_2.
#Time Complexiy, 2*O(V+E) using Kosaraju's algo to calculate SCCs and then O(E) to traverse over all edges. So, 2*O(V+E) + O(E) -> 2*O(V+E)  (2 as we do two DFSs in Kosaraju's, one one normal and one on transpose graph)

from collections import defaultdict 
   
#This class represents a directed graph using adjacency list representation 
class Graph: 
   
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = defaultdict(list) # default dictionary to store graph
        self.SCC = [0 for _ in range(self.V)]
        self.belong = [-1 for _ in range(self.V)]
        self.CCs = 0;
   
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
   
    # A function used by DFS 
    def DFSUtil(self,v,visited,curr): 
        # Mark the current node as visited and print it
        self.SCC[curr]+=1;
        self.belong[v] = curr; 
        visited[v]= True 
        #Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i]==False: 
                self.DFSUtil(i,visited,curr) 
  
  
    def fillOrder(self,v,visited, stack): 
        # Mark the current node as visited  
        visited[v]= True
        #Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i]==False: 
                self.fillOrder(i, visited, stack) 
        stack.append(v) #as per DFS
      
  
    # Function that returns reverse (or transpose) of this graph 
    def getTranspose(self): 
        k = Graph(self.V) 
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph: 
            for j in self.graph[i]: 
                k.addEdge(j,i) 
        return k 
  
   
   
    # The main function that finds and prints all strongly 
    # connected components 
    def printSCCs(self): 
        stack = []
        visited =[False]*(self.V) 
        # Fill vertices in stack according to their finishing 
        # times 
        for i in range(self.V): 
            if visited[i]==False: 
                self.fillOrder(i, visited, stack) 
  
        # Create a reversed graph 
        self.gr = self.getTranspose() 
           
         # Mark all the vertices as not visited (For second DFS) 
        visited =[False]*(self.V) 
  
         # Now process all vertices in order defined by Stack
        curr = -1;
        while stack: 
            i = stack.pop() #last element i.e. 0
            if visited[i]==False:
                curr+=1
                self.CCs+=1;
                self.gr.DFSUtil(i, visited,curr) 
    def increase(self):
      self.printSCCs()
      print(self.CCs)
      self.SCC = (self.gr.SCC)
      self.belong = (self.gr.belong)
      MAX = max(self.SCC)
      for i in range(self.V):
        for node in self.graph[i]:
          l,r = self.belong[i],self.belong[node]
          if  l!=r:
            curr = self.SCC[l] + self.SCC[r]
            MAX = max(MAX,curr)
      return MAX;
   
# Create a graph given in the above diagram 
g = Graph(5) 
g.addEdge(0, 1) 
g.addEdge(1, 2) 
g.addEdge(2, 3) 
g.addEdge(3, 1) 
g.addEdge(4, 0)
g.addEdge(0,4)

print(g.increase())
