
def quickSort(lyst):
    lyst, comparisonNumber=quicksortHelper(lyst, 0, len(lyst) - 1,0)
    return lyst, comparisonNumber

def quicksortHelper(lyst, left, right,comparisonNumber):
    comparisonNumber+=1
    if left < right:
        pivotLocation,comparisons = partition(lyst, left, right)
        comparisonNumber+=comparisons
        quicksortHelper(lyst, left, pivotLocation - 1,comparisonNumber)
        quicksortHelper(lyst, pivotLocation + 1, right,comparisonNumber)
    return lyst, comparisonNumber

def partition(lyst, left, right):

    comparisonNumber=0
    # Find the pivot and exchange it with the last item
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    # Set boundary point to first position
    boundary = left
    # Move items less than pivot to the left
    for index in range(left, right):
        comparisonNumber+=1
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            boundary += 1
    # Exchange the pivot item and the boundary item
    swap (lyst, right, boundary)
    return boundary,comparisonNumber

def swap(lyst, i, j):
    """Exchanges the items at positions i and j."""
    # You could say lyst[i], lyst[j] = lyst[j], lyst[i]
    # but the following code shows what is really going on
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp
