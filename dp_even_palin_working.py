import time
start_time = time.time()

string = "srkabacuc"
n = len(string)

dp = [[[-1]*26 for _ in range(n)] for _ in range(n)]

print(len(dp),len(dp[0]),len(dp[0][0]))

def f(s,p1,p2,last):   #put value of last some shitty thing in main call, anything excpet for 0-26
    if p1>= p2:
        return 0
    ans = dp[p1][p2][last]

    if ans!= -1:
        return ans

    ans = 0
    curr = ord(string[p1]) - ord('a')

    if s[p1] == s[p2] and curr!=last:
        ans = max(ans, 2 + f(s,p1 + 1,p2 - 1,curr))

    ans = max(ans, f(s,p1+1,p2,last))
    ans = max(ans,f(s,p1,p2-1,last))
    dp[p1][p2][last] = ans;   #comment out this line to check the differenc ein runtime for long strings...
    return ans

print(f(string,0,n-1,-1))    #longest even palindromic substring with no same adjacent characters except for the middle ones...
print("--- %s seconds ---" % (time.time() - start_time))
