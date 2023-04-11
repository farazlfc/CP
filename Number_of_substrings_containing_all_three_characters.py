from collections import defaultdict
class Solution:
    def numberOfSubstrings(self, s):
        #we get all occurences, then remainder will also have, so 1  + remaining length
        #then we keep pushing back from the start until possible, 1 + remaining length
        count = defaultdict(int)
        n = len(s)
        i = 0
        answer = 0
        start = 0
        while  i < n:
            curr = s[i]
            if curr in ["a", "b", "c"]:
                count[curr] += 1 #whenever something becomes positive, then only increment
                while start < i and  (count["a"] and count["b"] and count["c"]):
                    answer += 1 + n-1 - i
                    curr = s[start]
                    count[curr] -= 1
                    start += 1
            i +=1 
        return answer



        
