
def Heap(array, length, index,comparison):
    #build a heap with root at array [index], and heap nodes in array[index...length]
    #Assuming that the two children of node array[index] are heaps already.
    larger_index = index
    l_child = 2 * larger_index + 1
    r_child = 2 * larger_index + 2
    
    comparison+=1
    if l_child < length and array[larger_index] < array[l_child]:
        larger_index = l_child
    comparison+=1
    if r_child < length and array[larger_index] < array[r_child]:
        larger_index = r_child
    comparison+=1
    if larger_index != index:
        array[index], array[larger_index] = array[larger_index], array[index]

        Heap(array, length, larger_index,comparison)
    
    return comparison

def heapSort(lyst):
    comparison=0
    #print(range(len(lyst)-1, -1, -1))
    #(1) Build a heap based on the elements in array[ ];
    for i in range(len(lyst)-1, -1, -1):
        comparison=Heap(lyst, len(lyst), i, comparison)
    #(2) for i = n-1 down to 1
    for i in range(len(lyst)-1, 0, -1):
        #swap the element at root with the element in position i;
        lyst[i], lyst[0] = lyst[0], lyst[i]
        #restore the heap property for sub-array[0, …, i-1];
        comparison=Heap(lyst, i, 0,comparison)

    return lyst, comparison


