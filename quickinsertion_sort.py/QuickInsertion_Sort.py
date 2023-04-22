def insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_insertion_sort(arr, low, high, threshold):
    while low < high:
        if high - low + 1 <= threshold:
            insertion_sort(arr, low, high)
            break
        else:
            pivot_index = partition(arr, low, high)
            if pivot_index - low < high - pivot_index:
                quick_insertion_sort(arr, low, pivot_index - 1, threshold)
                low = pivot_index + 1
            else:
                quick_insertion_sort(arr, pivot_index + 1, high, threshold)
                high = pivot_index - 1

def hybrid_sort(arr, threshold=16):
    quick_insertion_sort(arr, 0, len(arr) - 1, threshold)

# Example usage
arr = [12, 11, 13, 5, 6, 7]
hybrid_sort(arr)
print(arr)  # Output: [5, 6, 7, 11, 12, 13]
