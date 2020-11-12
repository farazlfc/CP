from collections import defaultdict
from heapq import *

def djikstra(edges,f,t):
  g = defaultdict(list)
  for l,r,c in edges:
    g[l].append((c,r))
  q,seen,mins = [(0,f,())],set(),{f:0}
  while q:
    cost,v1,path = heappop(q)
    if v1 not in seen:
      seen.add(v1);
      path = tuple(list(path) + [v1])
      #path statement!

      for c,v2 in g.get(v1,()):
        if v2 in seen:
          continue;
        prev = mins.get(v2,None)
        next = cost + c;
        if prev is None or next < prev:
          mins[v2] = next;
          heappush(q,(next,v2,path))
  return mins;
#we get mins_a and mins_b
# minimum is mins_a[b]
#others is for every pair of curved u anc v, #check mins_a[u] + c(u,v) + mins_b[v] and 
#mins_b[u] + c(u,v) + mins_a[v]
