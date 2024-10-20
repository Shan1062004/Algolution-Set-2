def find_equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0

    for i, num in enumerate(arr):
        total_sum -= num
        if left_sum == total_sum:
            return i + 1 
        left_sum += num

    return -1

arr1 = [-7, 1, 5, 2, -4, 3, 0]
arr2 = [1, 2, 3]
arr3 = [1, 3, 5, 2, 2]

print("Equilibrium index of arr1:", find_equilibrium_index(arr1))  
print("Equilibrium index of arr2:", find_equilibrium_index(arr2))  
print("Equilibrium index of arr3:", find_equilibrium_index(arr3))  
