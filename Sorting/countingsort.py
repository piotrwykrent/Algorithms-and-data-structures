def countingsort(A,m):
    n=len(A)
    m=m+1
    B=[0]*n
    C=[0]*m
    for i in range(n):
        C[A[i]]+=1
    for i in range(1,m):
        C[i]=C[i]+C[i-1]
    for i in range(n-1,-1,-1):
        C[A[i]]-=1
        B[C[A[i]]]=A[i]
    return B

T = [1, 6, 7, 3, 2, 6, 8, 0, 1]
print(countingsort(T, max(T)))