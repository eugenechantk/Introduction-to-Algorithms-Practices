def build_max_heap(arr):
    heap_size = len(arr)-1
    for i in range(int(heap_size/2),-1,-1):
        max_heapify(arr,i)

def max_heapify(arr,i):
    l = i * 2 + 1
    r = i * 2 + 2
    heap_size = len(arr)-1
    if l <= heap_size and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    
    if r <= heap_size and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr,largest)

    return True

def main():
    test_arr = [4,1,3,2,16,9,10,14,8,7]
    build_max_heap(test_arr)
    return True

main()