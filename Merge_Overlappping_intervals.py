#array = ((6,8),(1,9),(2,5),(2,4),(4,7))
#array = sorted(array)
def func(array):
  answer = []
  n = len(array)
  print(array)
  i = 0
  while i < n-1:
    a,b = array[i][0],array[i][1]
    c,d = array[i+1][0],array[i+1][1]
    if (c>=a and c<=b):
      print(a,b,c,d)
      array[i] = None #will pop at end
      array[i+1] = ((min(a,c),max(b,d)))
      print(array)
    i+=1 #in either case
  for i,j in enumerate(array):
    if j!= None:
      answer.append(j)
  return(answer)

for _ in range(int(input())):
  n = int(input())
  array_ = list(map(int,input().split()))
  array = []
  for i in range(0,2*n-1,2):
    array.append((array_[i],array_[i+1]))
  answer = func(sorted(array))
  string = ""
  for ans in answer:
    print(ans)
    #string+= str(x) + " " + str(y) + " "
  #print(string[:-1])
