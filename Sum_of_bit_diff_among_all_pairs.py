def func(arr,n): 
  
    ans = 0  # Initialize result 
  
    # traverse over all poss. bit positions 
    for i in range(0, 32): 
      
        # count number of elements with the i'th bit set 
        count = 0
        for j in range(0,n): 
            if ( (arr[j] & (1 << i)) ):  #left shift bit to check if that bit is set(<< operator is used to left shift)
                count+=1
  
        # Add "count * (n - count) * 2" to the answer, 2 for (i,j) and (j,i).
        ans += (count * (n - count) * 2); 
      
    return ans 
  
# Main program
arr = [1, 3, 5] 
n = len(arr ) 
print(func(arr, n)) 
