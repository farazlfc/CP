arr = [[1,-2,1],[1,-1,1],[-2,-1,3]]
n =3
threshold = 3
prefix = [[0 for _ in range(n)]for _ in range(n)]

for i in range(n):
  prefix[i][0] = arr[i][0]
for j in range(1,n):
  prefix[0][j] += prefix[0][j-1] + arr[0][j]
for i in range(1,n):
  for j in range(1,n):
    prefix[i][j] += arr[i][j] + prefix[i][j-1];
for i in range(1,n):
  prefix[i][0] += prefix[i-1][0]
for i in range(1,n):
  for j in range(1,n):
    prefix[i][j] += prefix[i-1][j];
def isfine(dim):
  for i in range(0,n - dim + 1):
    upper,lower = i,i + dim
    for j in range(0,n - dim + 1):
      left,right = j,j+dim;
      base_sum = prefix[lower - 1][right - 1];
      if upper>0 and left>0:
        base_sum += prefix[upper-1][left-1]
        base_sum -= prefix[upper-1][right-1]
        base_sum -= prefix[lower-1][left - 1] 
      if upper == 0 and left == 0:
        pass;
      elif upper == 0:
        base_sum -= prefix[lower-1][left-1];
      elif left == 0:
        base_sum -= prefix[upper-1][right-1]
      if base_sum > threshold:
        return False;
  return True;

low,high = 1,n
ans = None;
while low<=high:
  mid = (low + high)//2 ;
  if isfine(mid):
    ans = low;
    low = mid + 1;
  else:
    high = mid - 1;

if ans == None:
  print("NONE")
else:
  print(ans);
print(prefix)
