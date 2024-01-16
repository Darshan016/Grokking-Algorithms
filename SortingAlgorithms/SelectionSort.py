def findSmallest(arr):
    smallest=arr[0]
    smallest_index=0
    for i in range(1,len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
            smallest_index=i
    return smallest_index

def selectionSort(arr):
    ans=[]
    for i in range(len(arr)):
        smallest=findSmallest(arr)
        ans.append(arr.pop(smallest))
    return ans

arr=[45,12,36,95,75]
print(selectionSort(arr))