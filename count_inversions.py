# count the number of inversions necessary to sort an array
# original problem assumed we're swapping inversions over and over
# giving O(n^2) runtime, but we use mergesort 

def mergeSort(arr, start, end):
    if start >= end:
        return 0 

    swaps = 0

    mid = (start + end) // 2

    swaps += mergeSort(arr, start, mid)
    swaps += mergeSort(arr, mid + 1, end)
    swaps += merge(arr, start, mid, end)

    return swaps

def merge(arr, start, mid, end):
    # merge two halves of the array together:
    # one is arr[start:mid], other is arr[mid+1:end]
    # count number of inversions necessary to do so...hm.
    swaps = 0



    # make two arrays to hold two halves
    n_left = mid - start + 1
    n_right = end - mid
    left = [None] * n_left
    right = [None] * n_right

    for i in range(n_left):
        left[i] = arr[start + i]
    for j in range(n_right):
        right[j] = arr[mid + j + 1]

    i = j = 0
    k = start

    # merge until gone through an entire list
    while i < n_left and j < n_right:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            # in this case we have some arr[x] > arr[y] but x < y,
            # so it's an inversion
            # ...I think
            swaps += 1

        k += 1

    # merge in remainder of other list.
    # if we're merging in the left list, it's not an inversion.
    # otherwise it is.
    while i < n_left:
        arr[k] = left[i]
        i += 1

    while j < n_right:
        arr[k] = left[j]
        j += 1
        swaps += 1

    return swaps

if __name__ == "__main__":
    arr1 = [8,4,2,1]
    arr2 = [1, 20, 6, 4, 5] 
    print(mergeSort(arr1, 0, len(arr1) - 1))
    print(mergeSort(arr2, 0, len(arr2) - 1))