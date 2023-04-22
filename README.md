# QuickInsertion Sort Algorithm

## Introduction
This repository contains the implementation of the QuickInsertion Sort algorithm, a hybrid sorting algorithm that combines the principles of QuickSort and Insertion Sort. The QuickInsertion Sort algorithm aims to achieve efficient and balanced sorting by taking advantage of the speed of QuickSort on larger datasets and the efficiency of Insertion Sort on smaller subarrays.

The algorithm includes a `threshold` parameter that specifies the size below which the algorithm switches from QuickSort to Insertion Sort.

## Implementation
The implementation is provided in the `quickinsertion_sort.py` file. It includes the following functions:
- `insertion_sort(arr, low, high)`: Performs insertion sort on a subarray.
- `partition(arr, low, high)`: Partitions the array for QuickSort.
- `quick_insertion_sort(arr, low, high, threshold)`: Recursive function that performs QuickSort with a threshold for switching to insertion sort.
- `hybrid_sort(arr, threshold=16)`: Main function for sorting an array using the QuickInsertion Sort algorithm.

## Example Usage
Here's an example of how to use the QuickInsertion Sort algorithm to sort an array of integers:

```python
from quickinsertion_sort import hybrid_sort

# Example array to be sorted
arr = [12, 11, 13, 5, 6, 7]

# Perform sorting using QuickInsertion Sort
hybrid_sort(arr)

# Output: [5, 6, 7, 11, 12, 13]
print(arr)
