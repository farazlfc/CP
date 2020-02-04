def f(s1,s2,a,b,k):
    #replace - b
    #add - a
    #remove - a
    m = len(s1)
    n = len(s2)
    if m == 0 and n == 0:
        return 0
    x = 1
    c = 1
        
    dp = [[0 for _ in range(n+1)]  for _ in range(2)]
    for i in range(0,n+1):
        dp[0][i] = a*i
    while c<= m:
        for i in range(0,n+1):
            if i == 0:
                dp[x][i] = c*a
            elif s1[c-1] == s2[i-1]:
                dp[x][i] = dp[1-x][i-1]  #mod this, think of cases
            else:
                dp[x][i] = min(dp[1-x][i-1] + b, dp[1-x][i] + a , dp[x][i-1]+a)
        c+=1
        x = 1-x   #this got changed at the end
    if dp[1-x][n] <= k:
        return dp[1-x][n]
    return -1

for _ in range(int(input())):
    s1 = input()
    s2 = input()
    a,b,k = tuple(map(int,input().split()))
    print(f(s1,s2,a,b,k))
    
