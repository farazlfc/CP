#https://leetcode.com/problems/range-sum-query-2d-immutable/description/
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n,m = len(matrix), len(matrix[0])
        for i in range(1, n):
            matrix[i][0] +=  matrix[i-1][0]

        for j in range(1, m):
            matrix[0][j] += matrix[0][j-1]

        for i in range(1, n):
            for j in range(1, m):
                matrix[i][j]+= matrix[i][j-1] + matrix[i-1][j] - matrix[i-1][j-1] #double counting addressed
        self.matrix = matrix
              

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        matrix = self.matrix
        if row1 == 0 and col1 == 0:
            return matrix[row2][col2]
        if row1 == 0:
            return matrix[row2][col2] - matrix[row2][col1-1] #jsut one subtraction, no double counting
        if col1 == 0:
            return matrix[row2][col2] - matrix[row1-1][col2] #same as here
        return matrix[row2][col2] - matrix[row1-1][col2] - matrix[row2][col1-1] + matrix[row1-1][col1-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
