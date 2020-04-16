#https://leetcode.com/problems/maximum-performance-of-a-team/
from heapq import heapify, heappush, heappop

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        works = []
        for s, e in zip(speed, efficiency):
            works.append((e, s))
        works.sort(reverse = True)
        res, team, cur_p, cnt = 0, [], 0, 0
        for ppl in works:
            heappush(team, ppl[1])
            cur_p += ppl[1]
            cnt += 1
            if cnt > k:
                cur_p -= heappop(team)
                cnt -= 1
            res = max(res, cur_p*ppl[0])
        return res % (10**9 + 7)
