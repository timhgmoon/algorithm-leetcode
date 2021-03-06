# def partition(arr, low, high):
#   i = (low - 1)
#   pivot = arr[high]

#   for j in range(low, high):
#     if arr[j] <= pivot:
#       i = i+1
#       arr[i], arr[j] = arr[j], arr[i]

#   arr[i+1], arr[high] = arr[high], arr[i+1]
#   return (i+1)

# def quickSort(arr, low, high):
#   if len(arr) < 2:
#     return arr
  
#   if low < high:
#     pi = partition(arr, low, high)

#     quickSort(arr, low, pi-1)
#     quickSort(arr, pi+1, high)
def quickSort(arr):
  if len(arr) < 2:
    return arr
  else:
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]

    return quickSort(less) + [pivot] + quickSort(greater)

arr = [10, 7, 8, 9, 1, 5]
print(quickSort(arr))
