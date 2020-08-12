# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
        # Your code here
        if( end >= start):
            mid = (end + start) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                return binary_search(arr, target, start, mid - 1)
            else:
                return binary_search(arr, target, mid + 1, end)
        else:
            return -1  # not found


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    pass
    # Your code here
