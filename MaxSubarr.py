def FindMaxCrossingSubarr(A, low, mid, high):
    left_sum = -1000
    sum = 0
    max_left = mid
    for i in reversed(range(low, mid + 1)): # from mid downto low
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = -1000
    sum = 0
    max_right = mid + 1
    for j in range(mid + 1, high + 1):
        sum = sum +A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return (max_left, max_right, left_sum + right_sum)

# O(n lgn)
def FindMaxSubarr(A, low, high):
    if high == low:
        return (low, high, A[low])
    else:
        mid = (low + high) // 2
        (left_low, left_high, left_sum) = FindMaxSubarr(A, low, mid)
        (right_low, right_high, right_sum) = FindMaxSubarr(A, mid + 1, high)
        (cross_low, cross_high, cross_sum) = FindMaxCrossingSubarr(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)

# O(n^2)
def FindMaxSubarrBruteForce(A):
    max_now = -1000
    low, high = 0, 0
    for i in range(len(A)):
        sum = 0
        for j in range(i, len(A)):
            sum = sum + A[j]
            if sum > max_now:
                max_now = sum
                low = i
                high = j

    return (low, high, max_now)

# O(n)
# Based on observation, max subarray is either A[1..j] or A[i..j+1]
# where 1 <= i <= j+1
def MaxSubarrLinear(A):
    max_sum = -1000
    ending_here_sum = -1000
    low, high, ending_here_low = 0, 0, 0
    for j in range(len(A)):
        ending_here_high = j
        if ending_here_sum > 0:
            ending_here_sum = ending_here_sum + A[j]
        else:
            ending_here_low = j
            ending_here_sum = A[j]

        if ending_here_sum > max_sum:
            max_sum = ending_here_sum
            low = ending_here_low
            high = ending_here_high
    return (low, high, max_sum)

A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
# A = [2, 3, 4, 5, 7]
# print(FindMaxSubarr(A, 0, len(A) - 1))
# print(FindMaxSubarrBruteForce(A))
print(MaxSubarrLinear(A))