#code
def answer(string):
    n = len(string)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    def get(string,i,j):
        if i==j:
            return 0
        if i+1 == j:
            if string[i] == string[j]:
                return 0
            else:
                return 1
        if i>j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if string[i] == string[j]:
            dp[i][j] = get(string,i+1,j-1)
            return dp[i][j]
        else:
            dp[i][j] = min(1+ get(string,i+1,j),1 + get(string,i,j-1))
        return dp[i][j]
    return get(string,0,n-1)
for _ in range(int(input())):
    print(answer(input()))
        
