class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        low,high = 0, n-1
        while low<=high:
            mid = low + (high - low)//2
            if arr[mid] == x:
                index =  mid
                break;
            elif arr[mid] > x:
                high = mid - 1
            else:
                low = mid + 1
        index = low;
        result = []
        if arr[index] == x:
            result.append(x)
            k-=1
            left,right = index - 1,index  +1
        elif arr[index] < x:
            left,right = index,index+1
        else:
            left,right = index-1,index
        while k>0:
            if right >= n:
                result = result +  arr[left-k+1:left+1][::-1]
                break;
            if left < 0:
                result = result + arr[right:right+k]
                break;
            if abs(arr[left] - x) <= abs(arr[right] - x):
                result.append(arr[left])
                left-=1
                k-=1
            else:
                result.append(arr[right])
                right+=1
                k-=1
        return sorted(result)
            
