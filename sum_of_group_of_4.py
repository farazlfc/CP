def fourSum(nums, target):
        if not nums: return []
        res = set()
        target = target
        cnt = 4
        nums = sorted(nums)

        def dfs(ns, path):
            path_len = len(path)
            path_sum = sum(path)
            if path_len > cnt:
                return
            if path_sum + sum(ns[:cnt-path_len]) > target: #optimization
                return
            if path_sum + sum(ns[path_len- cnt:]) < target:  #optimization
                return
            if cnt - len(path) == 2:
                l, r = 0, len(ns)-1
                while l < r:
                    s = ns[l] + ns[r]
                    if s == target - path_sum:
                        res.add(path+(ns[l], ns[r]))
                        while l < r and ns[l] == ns[l+1]:
                            l += 1
                        l += 1
                        while l < r and ns[r] == ns[r-1]:
                            r -= 1
                        r -= 1
                    elif s < target - path_sum:
                        l += 1
                    else:
                        r -= 1
                return  #cool
            for i, v in enumerate(ns):
                dfs(ns[i+1:], path+(ns[i],))
        dfs(nums, tuple())

        return [list(item) for item in res]

for _ in range(int(input())):
    n,target = tuple(map(int,input().split()))
    array = list(map(int,input().split()))
    array = sorted(array)
    answer = fourSum(array,target)
    if answer == []:
        print(-1)
        continue;
    answer = sorted(answer)
    str_ans = ""
    for arr in answer:
        for el in arr:
            str_ans += str(el)
            str_ans += " "
        str_ans += "$"
    print(str_ans)
