#https://www.spoj.com/problems/MKBUDGET/
def find(months,hire,fire,salary):
  n = len(months)
  MAX = max(months);
  dp = [[float("inf") for _ in range(MAX + 1)] for _ in range(n)]
  for i in range(months[0], MAX+1):
    dp[0][i] = (hire+salary)*(i)
  for i in range(1,n):
    if months[i] <= months[i-1]:
      for state in range(months[i], MAX + 1):  #all possible states
        for k in range(months[i-1], MAX + 1):  #all possible previous states
          if k>= state:   #if prev state >= current state, we need to fire people
            dp[i][state] = min(dp[i][state], dp[i-1][k] + (k-state)*fire + state*salary); 
          else:  #(curr_state > prev_state)  # we need to hire people
            dp[i][state] = min(dp[i][state], dp[i-1][k] + (state - k)*hire + state*salary); 
    else:
      for state in range(months[i] , MAX + 1):   #curr_emp > last_emp
        for k in range(months[i-1] , MAX + 1):
          if k>= state:
            dp[i][state] = min(dp[i][state], dp[i-1][k] + (k-state)*fire + state*salary);
          else:  #(curr_state > prev_state)  # we need to hire people
            dp[i][state] = min(dp[i][state], dp[i-1][k] + (state - k)*hire + state*salary);
  num_emps_last = months[-1]
  n = len(months); 
  answer  = float("inf")
  i = n-1;
  for state in range(months[n-1],MAX + 1):
    for k in range(months[i-1],MAX+1):
      if k>= state:
            dp[i][state] = min(dp[i][state], dp[i-1][k]+ state*salary);
      else:  #(curr_state > prev_state)  # we need to hire people
            dp[i][state] = min(dp[i][state], dp[i-1][k] + (state - k)*hire + state*salary);
  return min(dp[n-1]);
while True:
	temp = input()
	if temp == "0":
		break
	temp = list(map(int,temp.split()))
	hire,salary,fire = temp[1],temp[2],temp[3]
	months = temp[4:]
	print(find(months,hire,fire,salary))
		
