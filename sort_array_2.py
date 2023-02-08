import sys
def sort_arr(x,num):
    cnt = 0
    for i in range(len(x)-1,0,-1):
        max = i
        for j in range(0, i):
            if x[max] < x[j]:
                max = j
        if x[max] != x[i]:
            x[max],x[i] = x[i],x[max]
            cnt += 1
        if cnt == num:
            return x
    return -1
n,k = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
result = sort_arr(arr,k)
if result != -1:
    for i in result:
        print(i,end=" ")
else:
    print(result)