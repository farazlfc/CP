def driver(graph,visited):
    answer = []
    def func(source,count,visited,cost):
        if count == n:
            answer.append(cost + graph[source][0])
            return
        for i in range(n):
            if not visited[i] and graph[source][i]:
                visited[i] = True
                func(i,count+1,visited,cost + graph[source][i])
                visited[i] = False
    func(0,1,visited,0)
    return answer
for _ in range(int(input())):
    n = int(input())
    array = []
    numbers = list(map(int,input().split()))
    for i in range(n):
        array.append(numbers[i*n:(i+1)*n + 1])
    visited = [False]*n
    visited[0] = True
    print(min(driver(array,visited)))
        
