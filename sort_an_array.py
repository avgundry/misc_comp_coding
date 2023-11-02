# practicing merge sort
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, arr, start, end):
        if start >= end:
            return 

        mid = (start + end) // 2
        self.mergeSort(arr, start, mid)
        self.mergeSort(arr, mid + 1, end)
        self.merge(arr, start, mid, end)

    def merge(self, arr, start, mid, end):
        n_L = mid - start + 1
        n_R = end -  mid

        L = [None] * (n_L + 1)
        R = [None] * (n_R + 1)

        for i in range(n_L):
            L[i] = arr[start + i]

        for j in range(n_R):
            R[j] = arr[mid + j + 1]


        i = j = 0
        k = start

        while i < n_L and j < n_R:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1

            k += 1

        while i < n_L:
            arr[k] = L[i]
            i += 1
            k += 1
        while j < n_R:
            arr[k] = R[j]
            j += 1
            k += 1


if __name__ == "__main__":
    s = Solution()
    arr1 = [5,2,3,1]
    arr2 = [5,1,1,2,0,0]
    s.sortArray(arr1)
    print(arr1)
    s.sortArray(arr2)
    print(arr2)