class Solution:
    def numSquarefulPerms(self, A):
        def is_square(num):
            return num**0.5 == int(num**0.5)
        def search(so_far, used):
            if len(so_far) == len(A):
                self.res += 1
            for i in range(len(A)):
                # If A[i] is already used, go to the next i.
                if used[i]: 
                    continue
                # To avoid doing double-work for repeated elements.
                # i.e., if A[i] == A[i-1], A[i-1] should be always used first.
                elif i > 0 and A[i] == A[i-1] and not used[i-1]:
                    continue    
                if not so_far or is_square(A[i] + so_far[-1]):
                    used[i] = True
                    so_far.append(A[i])
                    search(so_far, used)
                    used[i] = False
                    so_far.pop()
        self.res = 0
        A.sort() # Make repeated elements adjacent 
        used = [False] * len(A)
        search([], used)
        return self.res
