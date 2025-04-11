def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example usage
if __name__ == "__main__":
    # Test arrays
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    arr2 = [64, 34, 25, 12, 22, 11, 90]
    arr3 = [64, 34, 25, 12, 22, 11, 90]
    
    print("Original array:", arr1)
    
    # Test insertion sort
    sorted_arr1 = insertion_sort(arr1.copy())
    print("Insertion Sort:", sorted_arr1)
    
    # Test selection sort
    sorted_arr2 = selection_sort(arr2.copy())
    print("Selection Sort:", sorted_arr2)
    
    # Test merge sort
    sorted_arr3 = merge_sort(arr3.copy())
    print("Merge Sort:", sorted_arr3)