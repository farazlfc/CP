class Solution:
    def max_hist(self,arr):
        n = len(arr)
        i = 0
        stack = []
        max_area = 0
        while i<n:
            if not stack or arr[stack[-1]] <= arr[i]:
                stack.append(i)
                i+=1
            else:
                top_of_stack = stack.pop()
                if stack:
                    area = (i-stack[-1]-1)*(arr[top_of_stack])
                    max_area = max(area,max_area)
                else:
                    area = (i)*(arr[top_of_stack])
                    max_area = max(area,max_area)
        while stack:
            top_of_stack = stack.pop()
            if stack:
                area = (arr[top_of_stack])*(i - stack[-1]-1)
            else:
                area = (arr[top_of_stack])*(i)
            max_area = max(area,max_area)
        return max_area
            
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        if n <= 0:
            return 0
        m = len(matrix[0])
        new = []
        for row in matrix:
            new.append(list(map(int,row)))
        matrix = new
        for i in range(m):
            for j in range(1,n):
                if matrix[j][i] >0:
                    matrix[j][i] += matrix[j-1][i]
                else:
                    pass
        max_area = 0
        for row in matrix:
            max_area = max(max_area,self.max_hist(row))
        return max_area
