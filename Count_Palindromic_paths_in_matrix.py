import numpy as np
def recurse(arr,dp,i,j,m,n,rows,cols):
    if dp[i][j][m][n] != -1:
        return dp[i][j][m][n]
    if i>m or j>n:
        dp[i][j][m][n] = 0;
        return 0
    if i==m and j==n:
        dp[i][j][m][n] = 1;
        return 1;
    if i == m:
        if j+1 == n:
            if arr[i][j] == arr[m][n]:
                dp[i][j][m][n] =1;
                return 1;
            else:
                dp[i][j][m][n] =0;
                return 0;
    if j == n:
        if i+1 == m:
            if arr[i][j] == arr[m][n]:
                dp[i][j][m][n] = 1;
                return 1;
            else:
                dp[i][j][m][n] =0;
                return 0;
    dp[i][j][m][n] = 0;
    if i+1 <= rows-1:
        if arr[i+1][j] == arr[m-1][n]:
            dp[i][j][m][n] += recurse(arr,dp,i+1,j,m-1,n,rows,cols)
        if arr[i+1][j] == arr[m][n-1]:
            dp[i][j][m][n] += recurse(arr,dp,i+1,j,m,n-1,rows,cols)
    if j+1 <= cols-1:
        if arr[i][j+1] == arr[m-1][n]:
            dp[i][j][m][n] += recurse(arr,dp,i,j+1,m-1,n,rows,cols)
        if arr[i][j+1] == arr[m][n-1]:
            dp[i][j][m][n] += recurse(arr,dp,i,j+1,m,n-1,rows,cols)
    
    return dp[i][j][m][n]

for _ in range(int(input())):
    rows,cols = tuple(map(int,input().split()))
    characters = np.array(input().split()).reshape((rows,cols))
    dp = [[[[-1 for _ in range(cols)]for _ in range(rows)]for _ in range(cols)]for _ in range(rows)]
    if characters[0][0] == characters[rows-1][cols-1]:
        print(recurse(characters,dp,0,0,rows-1,cols-1,rows,cols))
    else:
        print(0)
