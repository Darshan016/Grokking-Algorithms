def count(arr):
    if not arr:
        return 0
    else:
        return 1+count(arr[1:])

arr=[1,2,3]
print(count(arr))