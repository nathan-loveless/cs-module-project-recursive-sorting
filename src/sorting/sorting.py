# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(left, right):
    # Your code here
    sorted = []

    i = 0
    j = 0

    elements = len(left) + len(right)
    while len(sorted) < elements:
        if i >= len(left):
            sorted.append(right[j])
            j += 1
        elif j >= len(right):
            sorted.append(left[i])
            i += 1
        elif left[i] <= right[j]:
            sorted.append(left[i])
            i += 1
        elif left[i] >= right[j]:
            sorted.append(right[j])
            j += 1

    return sorted


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):


    # Your code here
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        l = merge_sort(left)
        r = merge_sort(right)
        arr = merge(l, r)

    return arr
    

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass
    # Your code here


def merge_sort_in_place(arr, l, r):
    pass
    # Your code here

