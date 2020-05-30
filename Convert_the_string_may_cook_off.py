from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    A = input()
    B = input()
    FLAG = False;
    boolean = [False]*26;   #to check presence of letter in A. Alternatively, can use set.
    index = [-1]*26         #index of letter in A
    taken = defaultdict(list)   #to store the moves.
    answer = [];               
    for i in range(n):
        boolean[ord(A[i]) - ord('a')] = True;
        index[ord(A[i]) - ord('a')] = i;
    for i in range(n):
        if A[i] != B[i]:
            BOOL = boolean[ord(B[i]) - ord('a')]
            if not BOOL:  #if not present, then not possible
                print(-1);
                FLAG = True;
                break;
            if A[i] > B[i]:    #OK condition
                taken[B[i]].append(i);
            else:    #not possible, only lower value alphabets can replace.
                print(-1);
                FLAG = True;
                break;
    if FLAG:
        continue;
    ops = 0   #number of moves
    for char in sorted(taken.keys())[::-1]:    #sorting is essential, as higher value ones should be taken care off first. 
        ops +=1;
        IND = index[ord(char) - ord('a')]
        if IND == -1:
            print(-1);
            FLAG = True;
            break;
        NEW = [IND]
        NEW = [len(taken[char]) + 1] + NEW + taken[char]
        answer.append(NEW)
    if FLAG:
        continue;
    print(ops)
    if ops == 0:
        continue;
    for temp in answer:
        print(" ".join(list(map(str,temp))))
                    
            

