def get_perimeter(n,m,farm):
    if n<1:
        return 0
    if m<1:
        return 0
    dp = [[0 for _ in range(m)] for _ in range(n)]
    #dp[0][0] =  farm[0][0]
    for i in range(n):
        for j in range(m):
            if  j == 0:
                dp[i][j] = farm[i][j]
            else:
                dp[i][j]+= dp[i][j-1] + farm[i][j]
    for j in range(m):
        for i in range(n):
            if  i == 0:
                dp[i][j] = dp[i][j]
            else:
                dp[i][j]+= dp[i-1][j]
    def factors_get(n):
        return list(set(factor for i in range(1, int(n**0.5) + 1) if n % i == 0 for factor in (i, n//i)))
    #dp is prefix array
    def find(area):
        maxi_perimeter = 0
        factors = factors_get(area)
        factors.append(area)
        for l in factors:
            b = area//l
            for i in range(n-l+1):
                for j in range(m-b+1):
                    total = 0
                    total+= dp[i+l - 1][j+b - 1]
                    if i>0:
                        total-= dp[i-1][j + b -1]
                    if j>0:
                        total-= dp[i+l-1][j-1]
                    if i>0 and j>0:
                        total+= dp[i-1][j-1]
                    if total == 0:
                        maxi_perimeter = max(maxi_perimeter, 2*(l+b))
        return maxi_perimeter
                    
    max_perimeter = 0
    area =  n*m
    for ar in range(1,area + 1):
        max_perimeter = max(find(ar),max_perimeter)
    
    return max_perimeter

for _ in range(int(input())):
    n,m = tuple(map(int,input().split()))
    farm = []
    for _ in range(n):
        farm.append(list(map(int,list(input()))))
    #print(farm)
    print(get_perimeter(n,m,farm))
    
    
