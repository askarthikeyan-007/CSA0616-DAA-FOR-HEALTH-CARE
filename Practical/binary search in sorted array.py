def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


X = [3, 4, 6, -9, 8, 9, 10, 30]
X.sort()  
key = 10
position = binary_search(X, key)
print(f"Element {key} is found at position {position}" if position != -1 else "Element not found")
