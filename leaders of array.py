def Leaders(arr):
    n = len(arr)
    l=[]
    for i in range(0,n):
        for j in range(i + 1,n):
            if arr[i] <= arr[j]:
                break
        if j == n- 1:
            l.append(arr[i])
    return l
arr = list(map(int,input('A=').split()))
print(Leaders(arr))