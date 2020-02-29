from collections import defaultdict
def get_answer(candies,personal):
  dp = defaultdict(lambda : -1) 
  def candy(rem,i,n):
    if dp[str(rem) + " " + str(i)] != -1:
      #print(rem,i)
      return dp[str(rem) + " " + str(i)]
    if rem<0:
      return 0
    if rem==0:
      return 1
    if i>=n:
      return 0
    ans = 0;
    for curr in range(0,personal[i] + 1):  #if i==n-1, then use up all rem?prolly
      ans+= candy(rem-curr,i+1,n)
    dp[str(rem) + " " + str(i)] = ans;
    return ans
  return candy(candies,0,len(personal))

n,candies = 3,4
personal = [1, 2, 3]
print(get_answer(candies,personal))
