

def merge(arr, left, mid, right):
    i = left
    j = mid + 1
    k = 0
    invCount = 0
    temp = [0] * (right - left + 1)
 
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            invCount += mid - i + 1
            k += 1
            j += 1
 
    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1
 
    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1
 
    for i in range(left, right + 1):
        arr[i] = temp[i - left]
 
    return invCount

def mergeSort(arr, left, right):
    invCount = 0
 
    if left < right:
        mid = (left + right) // 2
 
        invCount += mergeSort(arr, left, mid)
        invCount += mergeSort(arr, mid + 1, right)
        invCount += merge(arr, left, mid, right)
 
    return invCount
 
 
def getInversions(arr):
    n = len(arr)
    return mergeSort(arr, 0, n - 1)

def rockerPercent(arr):
    
    inversions = getInversions(arr)
    inversions = inversions - 45
    percent = round(-1*((inversions / 45) * 100),0)
    return percent
