def typeset(l, D, s):
    n = len(l)
    L = DenseMatrix(n, n)
    for i in range(n):
        L[i, i] = l[i]
        for j in range(i+1, n):
            L[i, j] = L[i, j-1] +l[j]
    P = DenseMatrix(n, n)
    for i in range(n):
        for j in range(j, n):
            if L[i, j] < D:
                P[i, j] = abs(D - L[i,j] -(j-i)*s)
            else:
                P[i, j] = sys.maxint
    c = DenseMatrix(n, n)
    for j in range(n):
        c[j, j] = P[j, j]
        i = j -1
        while i >= 0:
            min = P[i, j]
            for k in range(i, j):
                tmp = P[i, k] + c[k+1, j]
                if tmp < min:
                    min = tmp
            c[i, j] = min
            i -= 1
