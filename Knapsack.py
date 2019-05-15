def FractionalKnapsack(S, w, W):
    values = []
    knapsack = []
    for i in range(len(S)):
        values.append((S[i], w[i], S[i]//w[i]))
    values = sorted(values, key=lambda values: values[2])
    weight_curr = 0
    while weight_curr < W and values:
        item, weight, val = values[-1]
        weight = min(weight, W-weight_curr)
        knapsack.append((item, weight, val))
        weight_curr += weight
        values.pop()

    total_val = 0
    for item in knapsack:
        total_val += item[1] * item[2]
    return total_val

def Knapsack(S, wt, W):
    B = [[0 for _ in range(W + 1)] for _ in range(len(S) + 1)]
    C = [[0 for _ in range(W + 1)] for _ in range(len(S) + 1)]
    for k in range(1, len(S) + 1):
        for w in range(W + 1):
            if wt[k - 1] > w: # if this item bigger than allowed weight, can't add in knapsack
                B[k][w] = B[k - 1][w]
                C[k][w] = C[k - 1][w]
            else:
                B[k][w] = max(B[k - 1][w], B[k - 1][w - wt[k - 1]] + S[k - 1])
                C[k][w] = C[k - 1][w - wt[k - 1]] + S[k - 1]
    return B[len(S)]

# Use lesser space by eliminating C
def Knapsack2(S, wt, W):
    B = [0] * (W + 1)
    for k in range(1, len(S) + 1):
        for w in reversed(range(wt[k-1], W + 1)):
            if B[w - wt[k - 1]] + S[k - 1] > B[w]:
                B[w] = B[w - wt[k - 1]] + S[k - 1]


    return B

S = [3, 5, 8, 4, 10]
wt = [2, 4, 5, 3, 9]
W = 20
print(Knapsack(S, wt, W))
print(Knapsack2(S, wt, W))

# S = [12, 32, 40, 30, 50]
# w = [4, 8, 2, 6, 1] # [3,4,20,5,50]
# W = 10 # total weight allow
# print(FractionalKnapsack(S, w, W))