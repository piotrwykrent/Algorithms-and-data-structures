def solution(T):
    def merge(T, p, q, r):
        i = p
        j = q
        B=[]
        while i < q and j < r:
            if T[i][0] > T[j][0]:
                B.append(T[i])
                i += 1
            else:
                T[j][1] += q-i
                B.append(T[j])
                j += 1
        while i < q:
            B.append(T[i])
            i += 1
        while j < r:
            B.append(T[j])
            j += 1
        for t in range(len(B)):
            T[p+t] = B[t]

    def merge_sort(T, p, r):
        if r - p > 1:
            q = (p + r) // 2
            merge_sort(T, p, q)
            merge_sort(T, q, r)
            merge(T, p, q, r)

    def msort(T):
        dl = len(T)
        merge_sort(T, 0, dl)

    T = [[x, 0] for x in T]
    msort(T)
    return max(count[1] for count in T)
