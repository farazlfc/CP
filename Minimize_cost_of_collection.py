Cost to collection n coins,(one of each kind) arr gives cost to buy a certain coin and x is cost to change all current coins from i  to i+1. Initially we have 0 coins.
n,x = 4,5
arr = [6,1,3,2]  #1 + 5 + 5,1 + 5,1 => 1 + 1 + 1 + 5 + 5
dp = [[float("inf") for _ in range(n)] for _ in range(n)]
for i in range(n):
  dp[i][0] = arr[i];
for i in range(n):
  for j in range(1,n):  #distance
    index = i-j
    if index < 0:
      index = n + index;
    dp[i][j] = min(dp[i][j-1],arr[(index)%n])
MIN = float("inf");
for i in range(0,n):  #distance
  ans = 0;
  for j in range(0,n):   #index
    ans+= dp[j][i]
  ans += i*x
  print(ans,i)
  MIN = min(MIN,ans)
print(MIN)

