def mergeSort(arr, n, ref_arr):
    temp_arr = [0] * n
    return _mergeSort(arr, temp_arr, 0, n - 1, ref_arr)

def _mergeSort(arr, temp_arr, left, right, ref_arr):
    inv_count = 0

    if left < right:
        mid = (left + right) // 2

        inv_count += _mergeSort(arr, temp_arr, left, mid, ref_arr)
        inv_count += _mergeSort(arr, temp_arr, mid + 1, right, ref_arr)
        inv_count += merge(arr, temp_arr, left, mid, right, ref_arr)

    return inv_count

def merge(arr, temp_arr, left, mid, right, ref_arr):
    i = left
    j = mid + 1
    k = left
    inv_count = 0

    while i <= mid and j <= right:
        if ref_arr.index(arr[i]) <= ref_arr.index(arr[j]):
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            k += 1
            j += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]

    return inv_count

# Testando
arr = [10,9,8,7,6,5,4,3,2,1] # Input
ref_arr = [10,9,8,7,6,5,4,3,2,1]  # Array de referência
n = len(arr)
result = mergeSort(arr, n, ref_arr)
print("Number of inversions are:", result)
