def find_max(arr):
    if not arr:
        return 0
    else:
        return max(arr[0],find_max(arr[1:]))


arr=[55,7,96]
print(find_max(arr))