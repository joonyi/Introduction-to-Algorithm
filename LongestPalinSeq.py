def L(X, i, j):
    if i == j:
        return 1
    if X[i] == X[j]:
        if i + 1 == j:
            return 2
        else:
            return 2 + L(X, i+1, j-1)
    else:
        return max(L(X, i+1, j), L(X, i, j-1))

# X = 'character'
# X = "babad"
X = "cbbd"
print(L(X, 0, len(X)-1))