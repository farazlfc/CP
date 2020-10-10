n = 9 # total number of nodes  
graph = [[] for i in range(n+1)] 
graph[1].append(2)  
graph[1].append(3)  
graph[3].append(6)  
graph[2].append(4)  
graph[2].append(5)  
graph[5].append(7)  
graph[5].append(8)  
graph[5].append(9) 
#print(graph)
timer = 0
in_1 = [0 for i in range(n+1)]
out = [0 for i in range(n+1)]
visited = [False for _ in range(n+1)]
def dfs(v):
  global timer;
  visited[v] = True;
  timer+=1;
  in_1[v] = timer;
  for node in graph[v]:
    if not visited[node]:
      dfs(node)
  timer+=1;
  out[v] = timer
def query(x,y):
  if in_1[x] > in_1[y] and out[x] < out[y]:
    return True
  if in_1[y] > in_1[x] and out[y] < out[x]:
    return True
  return False
for node in range(1,n+1):
  if not visited[node]:
    dfs(node)
print(in_1)
print(out)
print(query(1, 5))
print(query(2, 9))
print(query(4, 6))
