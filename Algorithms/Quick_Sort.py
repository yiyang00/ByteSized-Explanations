# Quick Sort
def quicksort(A):
  if len(A) <= 1: # sequences that have a link of 1 and 0 do not require sorting, thus we use this to return the sequence
    return A
  else:
    pivot = A.pop() # .pop() removes the last element and returns it (which is now our pivot)
  # create 2 lists to move our items into after comparing them to the pivot value
  higher = [] # items greater than value of pivot
  lower = [] # items smaller than value of pivot

  for item in A: # use of for loop to compare every item in the sequence to the pivot
    if item > pivot:
      higher.append(item) # append the item to the list called 'higher'
    else: # includes items that are equal to pivot
      lower.append(item) # append the item to the list called 'lower'

  return quicksort(lower) + [pivot] + quicksort(higher) # concatenate the lower list, pivot, and higher list
  # use of recursion to keep running the algorithm until the logic of if len(A) not <= 1: the loop breaks
