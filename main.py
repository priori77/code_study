import sys
def select_sort(x, num):
    cnt = 0
    for i in range(len(x)-1,0,-1):
        max = i
        for j in range(0, i, 1):
            if x[j] > x[max]:
                max = j
        if x[i] != x[max]:
            x[i],x[max] = x[max], x[i]
            cnt += 1
        if cnt == num:
            return x[max],x[i]
    return -1

n, k = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
result = select_sort(arr,k)
if result != -1:
    for i in result:
        print(i,end = " ")
else:
    print(result)
