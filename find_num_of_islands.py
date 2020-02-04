#Given a boolean 2D matrix, find the number of islands. A group of connected 1s forms an island. For example, the below matrix contains 5 islands.
'''Input : mat[][] = {{1, 1, 0, 0, 0},
                   {0, 1, 0, 0, 1},
                   {1, 0, 0, 1, 1},
                   {0, 0, 0, 0, 0},
                   {1, 0, 1, 0, 1}
Output : 5'''

def get_islands(matrix):
    rows,cols = len(matrix),len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    def next_start():
        start = (-1,-1)
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] and not visited[i][j]:      #answer will be how many times we need to initialize start
                    start = (i,j)
                    break
        return start
    #if start[0] == n-1 and start[1] == m-1:
     #   return 1
    #if start[0] == -1:
     #   return 0          #get_next_1_func
    islands = 0
    stack = list()
    start_ = next_start()
    if start_ == (-1,-1):
        return 0
    islands+=1
    stack.append(start_)
    d1 = [1,-1,0]
    d2 = [1,-1,0]
    def isvalid(x,y):
        if x>=0 and y>=0 and x<rows and y<cols:
            return True
        return False

    while True:
        if len(stack) == 0:
            start_ = next_start()
            if start_ == (-1,-1):
                return islands
            else:
                stack.append(start_)
                islands+=1
        curr = stack.pop(-1)
        curr_x,curr_y = curr[0],curr[1]
        visited[curr_x][curr_y]  = True
        for p1 in d1:
            for p2 in d2:
                if isvalid(curr_x+p1,curr_y + p2) and matrix[curr_x+p1][curr_y + p2] and not visited[curr_x+p1][curr_y + p2]:
                    stack.append((curr_x+p1,curr_y + p2))
                    visited[curr_x+p1][curr_y + p2] =  True
    return islands

print(get_islands([[1, 1, 0, 0, 0],
                   [0, 1, 0, 0, 1],
                   [1, 0, 0, 1, 1],
                   [0, 0, 0, 0, 0],
                   [1, 0, 1, 0, 1]]))


