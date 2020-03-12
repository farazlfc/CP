'''Given a sorted dictionary of an alien language having N words and k starting alphabets of standard dictionary the task is to complete the function which returns a string denoting the order of characters in the language.
Note: Many orders may be possible for a particular test case, thus you may return any valid order.
Examples:
Input:  Dict[] = { "baa", "abcd", "abca", "cab", "cad" }, k = 4
Output: Function returns "bdac"
Here order of characters is 'b', 'd', 'a', 'c'
Note that words are sorted and in the given language "baa"
comes before "abcd", therefore 'b' is before 'a' in output.
Similarly we can find other orders.

Input: Dict[] = { "caa", "aaa", "aab" }, k = 3
Output: Function returns "cab"'''
from collections import defaultdict
dictionary = ["baa", "abcd", "abca", "cab", "cad" ]
k = 4
adj = defaultdict(list)
for i in range(1, len(dictionary)):
  word_1,word_2 = dictionary[i-1],dictionary[i]
  length = min(len(word_1),len(word_2))
  i = 0;
  while i<length:
    if word_1[i] != word_2[i]:
      adj[word_1[i]].append(word_2[i])
      break
    i+=1
#print(adj.keys())
print(adj)
in_rank = dict()
alpha = 'a'
nodes = []
for i in range(k):
  in_rank[alpha] = 0
  nodes.append(alpha)
  alpha = chr(ord(alpha) + 1) 
for node in adj.keys():
  for node_ in adj[node]:
    in_rank[node_]+=1 #could be done at once in above loop.
print(in_rank)
topo = []  #final ordering
queue = []
visited = [False]*k
for node in in_rank.keys():
    if in_rank[node] == 0:
      queue.append(node)
      visited[ord(node) - ord('a')] = True;
while len(queue):
  node = queue.pop(0)
  topo.append(node)
  for node_ in adj[node]:
    in_rank[node_]-=1 
  for node in in_rank.keys() :
    if in_rank[node] == 0 and not visited[ord(node)-ord('a')]:
      queue.append(node)
      visited[ord(node)-ord('a')] = True;
print(topo)   #prints bdac


    

