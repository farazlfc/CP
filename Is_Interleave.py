def isInterleave(self, A, B, C):
        #global k;
        n =len(A)
        m = len(B)
        k = len(C)
        if n + m != k:
            return 0
        def recurse(i,j,curr):
            #global k;
            if curr >= k:
                return 1
            a,b = 0,0
            if i < n:
                if A[i] ==  C[curr]:
                    a = recurse(i+1,j,curr+1)
                    #flag = True
            if j < m:
                if B[j] == C[curr]:
                    b = recurse(i,j+1,curr+1)
                    #flag = True
            return max(a,b)
        return recurse(0,0,0)

