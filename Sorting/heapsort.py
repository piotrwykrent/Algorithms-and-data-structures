def parent(i): return (i-1)//2
def left(i): return i*2+1
def right(i): return i*2+2

def heapify(A,n,i):                                                                     #5
    max_index=i                                                                     #10     12
    if left(i)<n and A[left(i)]>A[max_index]:
        max_index=left(i)
    if right(i)<n and A[right(i)]>A[max_index]:
        max_index=right(i)
    if max_index != i:
        A[i],A[max_index]=A[max_index],A[i]
        heapify(A,n,max_index)

def build_heap(A):
    n=len(A)
    for i in range(parent(n-1),-1,-1):
        heapify(A,n,i)

def heap_sort(A):
    build_heap(A)
    n=len(A)
    for i in range(n-1):
        A[0],A[n-i-1]=A[n-i-1],A[0]
        heapify(A,n-i-1,0)
    return A

A = [42, -5, 12, 0, 88, 12, -10, 7, 33, 105, -2, 42, 18, 90, 4, 1, 0, 55, -20, 14, 67, 3, 9, 11, 22, -8, 30, 41, 5, 12, 0, 100, 2, 45, 17, 31, -15, 8, 19, 21, 6, 13, 25, 36, 49, -1, 72, 81, 15, 20]
print(heap_sort(A))

