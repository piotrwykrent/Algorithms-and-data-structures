def solution(T):
    def merge(T, B, p, q, r):
        i = p
        j = q
        k = p
        while i < q and j < r:
            if T[i][0] >= T[j][0]:
                B[k] = T[i]
                i += 1
            else:
                T[j][1] += q - i
                B[k] = T[j]
                j += 1
            k += 1
        while i < q:
            B[k] = T[i]
            i += 1
            k += 1
        while j < r:
            B[k] = T[j]
            j += 1
            k += 1
        for t in range(p,r):
            T[t] = B[t]

    def merge_sort(T, B, p, r):
        if r - p > 1:
            q = (p + r) // 2
            merge_sort(T, B, p, q)
            merge_sort(T, B, q, r)
            merge(T, B, p, q, r)
    T = [[x, 0] for x in T]
    dl=len(T)
    B=[None]*dl
    merge_sort(T,B,0,dl)
    return max(count[1] for count in T)
