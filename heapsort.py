"""
Building a max heap: making sure that A[Parent(i)] >= A[i] at every i
"""
def build_max_heap(arr):
    heap_size = len(arr)-1
    # only need to traverse half of the node in the heap; only half of the nodes have children nodes
    for i in range(int(heap_size/2),-1,-1):
        max_heapify(arr,i)

"""
Max Heapify: making sure that the node at A[i] >= A[Left(i)] and A[Right(i)], Left(i) and Right(i) being A[i]'s two children node
"""
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
        # only swap places with the largest value node when finish comparing both left and right child
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr,largest)

    return True

def main():
    test_arr = [4,1,3,2,16,9,10,14,8,7]
    build_max_heap(test_arr)
    return True

main()