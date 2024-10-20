def max_length_subarray_with_sum(nums, target):
    sum_indices = {}
    current_sum = 0
    max_length = 0
    start_index = 0
    
    for i in range(len(nums)):
        current_sum += nums[i]
        
        if current_sum == target:
            max_length = i + 1
            start_index = 0
        
        if (current_sum - target) in sum_indices:
            if i - sum_indices[current_sum - target] > max_length:
                max_length = i - sum_indices[current_sum - target]
                start_index = sum_indices[current_sum - target] + 1
        
        if current_sum not in sum_indices:
            sum_indices[current_sum] = i
    
    return nums[start_index:start_index + max_length] if max_length > 0 else []

nums = [5, 6, -5, 5, 3, 5, 3, -2, 0]
target = 8
result = max_length_subarray_with_sum(nums, target)
print("The longest subarray with sum", target, "is:", result)
