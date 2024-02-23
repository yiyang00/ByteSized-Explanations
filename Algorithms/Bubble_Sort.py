# Bubble Sort
def bubble(A):
  sorted = False  # we would use this sorted variable later on to break us out of the loop when the list is sorted
  while not sorted:   # since we don't know the number of iterations we need to perform, we use a while loop
    sorted = True # this line is saying the list is sorted unless otherwise proven not sorted by the iteration below
    for i in range(0, len(A)-1): # indexing length up only to 2nd last index as we are unable to compare last element since there's no value to its right
      if A[i] > A[i+1]: # if left value greater than the right value
        sorted = False # it would just mean the list is still unsorted, thus sorted = False again
        A[i], A[i+1] = A[i+1], A[i] # position swap
  return A
