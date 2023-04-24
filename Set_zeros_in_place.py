#https://leetcode.com/problems/set-matrix-zeroes/
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n,m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    continue
                if i == 0 and j == 0:
                    continue
                if  j == 0:
                    if matrix[i-1][j] in [0, "a"]:
                        matrix[i][j] = "a"
                if i == 0:
                    if matrix[i][j-1] in [0, "b"]:
                        matrix[i][j] = "b"
                if i > 0 and  j > 0:
                    if matrix[i-1][j] in [0,"a"] and matrix[i][j-1] in [0,"b"]:
                        matrix[i][j] = 0 #OG
                    elif matrix[i-1][j] in [0,"a"]:
                        matrix[i][j] = "a"
                    elif matrix[i][j-1] in [0,"b"]:
                        matrix[i][j] = "b"
                    else:
                        pass
        for i in range(n-1, -1,-1):
            for j in range(m-1, -1, -1):
                if matrix[i][j] == 0:
                    continue
                if i == n-1 and j == m-1:
                    continue
                if j == m-1:
                    if matrix[i+1][j] in [0, "a"]:
                        matrix[i][j] = "a"
                if i == n-1:
                    if matrix[i][j+1] in [0, "b"]:
                        matrix[i][j] = "b"

                if i < n-1 and  j < m-1:
                    if matrix[i+1][j] in [0,"a"] and matrix[i][j+1] in [0,"b"]:
                        matrix[i][j] = 0
                    elif matrix[i+1][j] in [0,"a"]:
                        matrix[i][j] = "a"
                    elif matrix[i][j+1] in [0,"b"]:
                        matrix[i][j] = "b"
                    else:
                        pass
        for i in range(n):
            for j in range(m):
                if matrix[i][j] in ["a","b"]:
                    matrix[i][j] = 0
        return matrix
                





