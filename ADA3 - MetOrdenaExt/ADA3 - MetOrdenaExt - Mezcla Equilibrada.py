def merge_sort_equilibrada(arr):
    width = 1
    n = len(arr)
    while width < n:
        left = 0
        while left < n:
            right = min(left + (width * 2), n)
            mid = min(left + width, n)
            merge(arr, left, mid, right)
            left += width * 2
        width *= 2

def merge(arr, left, mid, right):
    left_half = arr[left:mid]
    right_half = arr[mid:right]
    i = j = 0
    k = left
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

arr = [38, 27, 43, 3, 9, 82, 10]

merge_sort_equilibrada(arr)
print("Lista ordenada:", arr)
