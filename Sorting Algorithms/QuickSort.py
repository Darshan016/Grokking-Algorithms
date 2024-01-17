def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        lesser = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


arr = [4, 2, 9, 66, 4, 75, 7]
print(quick_sort(arr))
