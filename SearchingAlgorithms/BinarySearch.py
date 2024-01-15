def binarySearch(arr,key):
    low=0
    high=len(arr)-1

    while low<=high:
        mid=(low+high)
        guess=arr[mid]
        if guess==key:
            return mid
        elif guess > key:
            high=mid-1
        else:
            low=mid+1
    return None

arr=[15,17,20,25,35,50,129,225]
print(binarySearch(arr,500))
