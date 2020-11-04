#BIT[100005], a[100005], n;

BIT = [0 for _ in range(10000005)]
def update(x,delta):
      while x<=n:  
        BIT[x] += delta;
        x += x&-x

def query(x):
     sum = 0;
     while x>0:
        sum += BIT[x];
        x -= x&-x
     return sum;
 
 
def getCount(number,i):
    left = query(number-1);
    right = i - query(number);
    if left < right:
      return 2*left  +1
    return 2*right + 1

def minimumOperations(numbers):
    ans=0;
    global n;
    n = max(numbers) + 1; # safe side
    length = len(numbers);
    #for(int i=0;i<numbers.size();i++){
    #     n = max(n, numbers[i]);
    #}
    
    for i in range(length):
        ans += getCount(numbers[i], i);
        update(numbers[i],1);
    return ans;
print(minimumOperations([2,4,1,3]))
