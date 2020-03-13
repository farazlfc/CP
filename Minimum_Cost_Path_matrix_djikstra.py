for _ in range(int(input())):
    n = int(input())  #n*n is the matrix
    cost = list(map(int,input().split())) #cost[row*col_size + col] -> formula to acces cost for each cell
    dist = [[float("inf") for _ in range(n)] for _ in range(n)] #to store min cost distance to reach each cell, using djikstra's
    dx = [-1,0,0,1] #movement vector in x direction
    dy = [0,1,-1,0] #   ""      ""   "" y    ""
    dist[0][0] = cost[0] #cost[0*n + 0]
    def isvalid(x,y,n):
        if x<0 or x>n-1:
            return False
        if y<0 or y>n-1:
            return False
        return True
    stack = []
    stack.append((0,0,dist[0][0]))
    while len(stack):
        x,y,dist_ = stack.pop(-1)  #dfs vs bfs?
        for i in range(len(dx)):  #check all the neighbours
            x2,y2 = x + dx[i],y + dy[i]
            if not isvalid(x2,y2,n): #if not a valid point
                continue
            curr_dist = cost[(x2)*n + y2] + dist_
            if curr_dist < dist[x2][y2]:   #if curr_dist less, then update min distance to reach that cell
                dist[x2][y2] = curr_dist
                stack.append((x2,y2,curr_dist)) #otherwise, the loop will run indefinitely
    
    print(dist[n-1][n-1])  #min distance to reach final cell
                
            
            
        
