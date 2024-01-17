def array_sum(arr):
    if not arr:
        return 0
    else:
        return arr[0] + array_sum(arr[1:])


arr = [1, 2, 3, 4]
print(array_sum(arr))
