def merge(A,B,p,q,r):
    i=p
    j=q
    k=p
    while i<q and j<r:
        if A[i]<=A[j]:
            B[k]=A[i]
            i+=1
        else:
            B[k]=A[j]
            j+=1
        k+=1
    while i<q:
        B[k]=A[i]
        i+=1
        k+=1
    while j<r:
        B[k]=A[j]
        j+=1
        k+=1
    for t in range(p,r):
        A[t]=B[t]

def merge_sort(A,B,p,r):
    if r-p>1:
        q=(p+r)//2
        merge_sort(A,B,p,q)
        merge_sort(A,B,q,r)
        merge(A,B,p,q,r)

def msort(A):
    n=len(A)
    B=[0]*n
    merge_sort(A,B,0,n)
    return A

A = [42, -5, 12, 0, 88, 12, -10, 7, 33, 105, -2, 42, 18, 90, 4, 1, 0, 55, -20, 14, 67, 3, 9, 11, 22, -8, 30, 41, 5, 12, 0, 100, 2, 45, 17, 31, -15, 8, 19, 21, 6, 13, 25, 36, 49, -1, 72, 81, 15, 20]
print(msort(A))
