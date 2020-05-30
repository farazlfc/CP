from collections import deque

def readTree(n):
    adj = [set() for _ in range(n)]
    for _ in range(n-1):
        u,v = map(int, input().split())
        adj[u-1].add(v-1)
        adj[v-1].add(u-1)
    return adj



def main():
    def solve():
        n,q = map(int, input().split())
        aa = [int(a) for a in input().split()]
        adj = readTree(n)
        dq = deque()
        dq.append(0)
        parent = [-2] + [-1] * (n-1)
        depth = [0] * n
        while dq:
            nd = dq.popleft()
            for a in adj[nd]:
                if parent[a] < 0:
                    parent[a] = nd
                    depth[a] = depth[nd] + 1
                    dq.append(a)

        def solve1():

            a,b = map(int, input().split())
            a -= 1
            b -= 1
            values = set()
            if depth[b] > depth[a]:
                b,a = a,b
            while depth[a] > depth[b]:   #equalize depth first.
                if aa[a] in values:
                    print(0)
                    return
                values.add(aa[a])
                a = parent[a]
            while a != b:   #take one step from each side.
                if aa[a] in values:  #can use bisect and sorted array to reduce time.
                    print(0)
                    return
                values.add(aa[a])
                a = parent[a]
                if aa[b] in values:
                    print(0)
                    return
                values.add(aa[b])
                b = parent[b]
            if aa[a] in values:
                print(0)
                return
            values.add(aa[a])
            lv = list(values)
            lv.sort()
            mn = n
            for i in range(len(lv)-1):
                mn = min(lv[i+1] - lv[i], mn)
                if mn == 1:
                    break
            print(mn)


        for _ in range(q):
            solve1()

    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
