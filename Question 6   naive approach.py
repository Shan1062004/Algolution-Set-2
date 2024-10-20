def has_pair_with_sum_naive(A, N, X):
    for i in range(N):
        for j in range(i + 1, N):
            if A[i] + A[j] == X:
                return True
    return False


A = [1, 2, 4, 5, 7, 11]
N = 6
X = 9
print("Naive Approach: ", has_pair_with_sum_naive(A, N, X)) 
