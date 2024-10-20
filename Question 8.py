def max_sum_of_k_consecutive_elements(arr, n, k):
    if k > n:
        return "Invalid"
    
    max_sum = sum(arr[:k])
    window_sum = max_sum

    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Example usage
arr1 = [100, 200, 300, 400]
arr2 = [1, 4, 2, 10, 23, 3, 1, 0, 20]
arr3 = [2, 3]

print("Max sum for arr1:", max_sum_of_k_consecutive_elements(arr1, len(arr1), 2))
print("Max sum for arr2:", max_sum_of_k_consecutive_elements(arr2, len(arr2), 4))  
print("Max sum for arr3:", max_sum_of_k_consecutive_elements(arr3, len(arr3), 3))  
