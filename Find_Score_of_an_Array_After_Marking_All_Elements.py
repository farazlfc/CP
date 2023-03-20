from collections import defaultdict
class Solution:
    def findScore(self, nums: List[int]) -> int:
        #We mark the first one and we need its neighbours, so we need to spot it in the array
        n = len(nums)
        score = 0
        sorted_nums = [(num, i) for i,num in enumerate(nums)]
        sorted_nums.sort()
        boolean = defaultdict(lambda : False)
        for i,(num, index) in enumerate(sorted_nums):
            if nums[index] < 0:
                continue
            else:
                score += num
                left, right = index - 1, index + 1
                if left >=0 and nums[left] > 0:
                    #score += nums[left]
                    nums[left] = -1
                if right < n and not boolean[right]:
                    #score += nums[right]
                    nums[right] = -1
        return score
        
        
