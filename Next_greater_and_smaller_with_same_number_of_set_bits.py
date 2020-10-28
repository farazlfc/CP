n= 5
def func_greater(n):
  repr = bin(n)[2:]
  length = len(repr)
  #next greater with same bits is -> if gap bw leftmost and right nearest then +1.
  if 2**(length) - 1 == n:
    return (int(repr[0] + "0" + repr[1:],2))
  right_first = None;
  for i in range(length-1,0,-1):
    if repr[i] == "1":
      right_first = i
    if repr[i] == "0":
      if right_first is not None:
        left_found = i
        break;
  new_str = repr[:left_found] + repr[right_first] + repr[left_found + 1:right_first] + repr[left_found] + repr[right_first+1:]
  #repr[right_first],repr[left_found] = repr[left_found],repr[right_first]
  return (int(new_str, 2))

def func_smaller(n):
  repr = bin(n)[2:]
  length = len(repr)
  if 2**(length) - 1 == n:
    return (n)
  right_first = None
  for i in range(length-1,-1,-1):
    if repr[i] == "0":
      right_first = i
    if repr[i] == "1":
      if right_first is not None:
        left_found = i
        break;
  new_str = repr[:left_found] + repr[right_first] + repr[left_found + 1:right_first] + repr[left_found] + repr[right_first+1:]
  #repr[right_first],repr[left_found] = repr[left_found],repr[right_first]
  return (int(new_str, 2))
answer = func_greater(3)
answer_1 = func_smaller(16)
print("Greater with same amount of set bits")
print(answer)
print("Smaller with same amount of set bits")
print(answer_1)
