'''Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.'''
#https://leetcode.com/problems/jump-game-iv/

class Solution:
    def minJumps(self, arr: List[int]) -> int:

        lookup = collections.defaultdict(set)
        for i, a in enumerate(arr):
            lookup[a].add(i)    #dict to store indices for a value
        
        q = [0]
        lookup[arr[0]].remove(0)
        dis = 0
        
        while q:
            tmp_q = []
            while q:
                idx = q.pop()
                if idx == len(arr)-1:
                    return dis
                for i in lookup[arr[idx]]:
                    tmp_q.append(i)
                lookup[arr[idx]] = []
                for i in [idx+1, idx-1]:
                    if i in lookup[arr[i]]:
                        lookup[arr[i]].remove(i)
                        tmp_q.append(i)
            q = tmp_q
            dis += 1  #once this layer completes;
        return False
