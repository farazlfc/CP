def driver(arr,k):
  if sum(arr)%k != 0:
    return -1
  target = sum(arr)//k
  num = len(arr)
  def func(curr_sum,n,boolean,el):
    if num - el < k-n: #terminate
      return False
    if el >= num:
      if n == k and curr_sum == 0:
        return True
      return False
    if n==k:
      return False
    answer = False
    for i in range(len(arr)):
      if not boolean[i]:
        if curr_sum + arr[i] == target:
          boolean[i] = True;
          answer = answer or func(0,n+1,boolean,el+1)
          boolean[i] = False
        elif curr_sum + arr[i] < target:
          boolean[i] = True;
          answer = answer or func(curr_sum + arr[i],n,boolean,el+1)
          boolean[i] = False
        else:
          continue
    return answer
  ans = func(0,0,[False]*num,0)
  return ans

print(driver([12,5,24,3,12,6,3,7],3))
