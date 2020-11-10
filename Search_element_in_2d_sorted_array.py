mat = [[10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50]];
print(mat)
val = 26 + 13;
n = 4;
i,j = 0,n-1
flag = 0;
while j>=0 and i<n:
  if mat[i][j] == val:
    flag = 1
    print(i,j)
    break;
  elif mat[i][j] > val:
    j-=1;
  else:
    i+=1;
if not flag:
  print("Not there")
