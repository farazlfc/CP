def get_min_path(values,characters,n,m):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    char_dp = [["" for _ in range(m)] for _ in range(n)]
    dp[0][0] = values[0][0]
    char_dp[0][0] = characters[0][0]
    for i in range(1,m):
        dp[0][i]+= dp[0][i-1] + values[0][i]
        char_dp[0][i]+= char_dp[0][i-1] + characters[0][i]
    for i in range(1,n):
        dp[i][0]+= dp[i-1][0] + values[i][0]
        char_dp[i][0]+= char_dp[i-1][0] + characters[i][0]
    for i in range(1,n):
        for j in range(1,m):
            if dp[i-1][j] > dp[i][j-1]:
                dp[i][j]+= dp[i][j-1] + values[i][j]
                char_dp[i][j] += char_dp[i][j-1] + characters[i][j]
            elif dp[i-1][j] < dp[i][j-1]:
                dp[i][j]+= dp[i-1][j] + values[i][j]
                char_dp[i][j] += char_dp[i-1][j] + characters[i][j]
            else:
                if char_dp[i-1][j] > char_dp[i][j-1]:
                    char_dp[i][j] += char_dp[i][j-1] + characters[i][j]
                else:
                    char_dp[i][j] += char_dp[i-1][j] + characters[i][j]
                dp[i][j]+= dp[i-1][j] + values[i][j]
    
    return dp[n-1][m-1],char_dp[n-1][m-1]

for _ in range(int(input())):
    n,m = tuple(map(int,input().split()))
    values = []
    characters = []
    for _ in range(n):
        values.append(list(map(int,input().split())))
    for _ in range(n):
        characters.append(list(input()))
    a1,a2 = get_min_path(values,characters,n,m)
    print(a1)
    print(a2)
            
            
