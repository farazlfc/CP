n = 7778393
def get_digits(n):
  answer = []
  while n>0:
    temp = n%10
    answer.append(temp)
    n = n//10
  return answer[::-1]
def way_1(n):   #sum of digits of all numbers from 1 to n
  digits = get_digits(n)
  length = len(digits)
  MAX = 9*(length + 1)
  dp = [[[None for _ in range(2)] for _ in range(MAX)] for _ in range(length + 1)]
  def recurse(index,SUM,bound):
    if index == length:
      return SUM
    if dp[index][SUM][bound] is not None:
      return dp[index][SUM][bound]
    curr = digits[index]
    if bound:
      end = curr
    else:
      end = 9
    ans = 0
    for digit in range(end + 1):
      if bound and digit == end:
        ans+= recurse(index + 1,SUM + digit,1)
      else:
        ans+= recurse(index + 1,SUM + digit,0)
    dp[index][SUM][bound] = ans;
    return ans

      

  curr = digits[0]
  ans = 0
  for digit in range(0,curr + 1):
    if digit == curr:
      new_bound = 1
      ans+= recurse(1,digit,new_bound)
    else:
      new_bound = 0
      ans+= recurse(1,digit,new_bound)
  return(ans);
print(way_1(n))
