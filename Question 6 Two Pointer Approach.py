def has_pair_with_sum_two_pointers(A, N, X):
    left = 0
    right = N - 1
    
    while left < right:
        current_sum = A[left] + A[right]
        if current_sum == X:
            return True
        elif current_sum < X:
            left += 1
        else:
            right -= 1
    
    return False

A = [1, 2, 4, 5, 7, 11]
N = 6
X = 9
print("Two Pointer Technique: ", has_pair_with_sum_two_pointers(A, N, X))  
