def isScramble(A, B):
        def scramble(s1,s2):
            if len(s1) != len(s2):
                return False
            if s1 == s2:
                return True
            if sorted(s1) != sorted(s2):
                return False
            for i in range(1,len(s1)):
                if (scramble(s1[:i],s2[:i]) and scramble(s1[i:],s2[i:])) or (scramble(s1[:i],s2[-i:]) and scramble(s1[i:],s2[:-i])):
                    return True
            return False
        return int(scramble(A,B))
