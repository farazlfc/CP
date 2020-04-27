#https://www.codechef.com/RC122020/problems/RECNDROT
def findM(A, n):
    elemIdxMap = dict()
    for i in range(n):
        if A[i] in elemIdxMap:
            elemIdxMap[A[i]].append(i)
        else:
            elemIdxMap[A[i]] = [i]
    
    keys = sorted(elemIdxMap.keys())
    
    # print(elemIdxMap, keys)

    connected = False
    count = 0
    prevIdx = -1

    nKeys = len(keys)
    for i in range(nKeys-1):
        
        if not connected:
            prevIdx = elemIdxMap[keys[i]][0]
            
            for idx in elemIdxMap[keys[i+1]]:
                if idx >prevIdx:
                    connected = True
                    count += 1
                    prevIdx = idx
                    break
        else:
            connected = False

            for idx in elemIdxMap[keys[i+1]]:
                if idx > prevIdx:
                    connected = True
                    count += 1
                    prevIdx = idx
                    break

        # print(keys[i], count, prevIdx)
    # if count == nKeys - 1:
    #     return 1
    # else:
    #     return (nKeys - count)
    # print(nKeys, count)
    return (nKeys - count)


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        A = list(map(int, input().split()))
        
        print(findM(A, n))
        # print(findM([1, 3, 2, 1, 2], 5))
        

