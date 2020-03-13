# d-f f-j f-k k-f f-k  n-f j-l l-z z-d
from collections import defaultdict
def func(array):
    adj = defaultdict(list)
    in_deg,out_deg = [0]*26,[0]*26
    for word in array:
        adj[ord(word[0])-ord('a')].append(ord(word[-1]) - ord('a'))
        out_deg[ord(word[0]) - ord('a')]+=1
        in_deg[ord(word[-1])-ord('a')]+=1  #indeg should be equal to outdeg
    for i in range(26):
        if in_deg[i]!= out_deg[i]:
            return False
    #second check is whether it is a single strongly connec. comp.
    visited = [False]*26
    source = list(adj.keys())[0]
    #print(source)
    #visited[source] = True
    stack = [source]  #dfs
    while len(stack): #or while stack,either will work.
        node = stack.pop(-1)
        visited[node] = True
        for node_ in adj[node]:
            if not visited[node_]:
                stack.append(node_)
        
    for i in range(26): #final check
        if not visited[i] and in_deg[i] > 0:
            return False
    return True

sample_array = ["for", "geek", "rig", "kaf"]
arr_false = ["for", "geek", "rig", "kaf","geek"]
arr_true = ["akc","cad","dln","nkc","dyz","zla","ceud"] 
print(func(sample_array))
print(func(arr_false))
print(func(arr_true))
