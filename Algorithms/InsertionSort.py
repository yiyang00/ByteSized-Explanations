# Insertion Sort

def insertion_sort(A):  # parameter A is the list input
  for i in range(1, len(A)):  # indexing length from 1 to the length of the list as index 0 is already in the sorted sublist
    key = A[i]
    while A[i-1] > key and i > 0: # 2 conditions: value to left higher than value to the right ...... also i has to be greater than 0 as python allows negative indexing
      A[i], A[i-1] = A[i-1], A[i] # position swap
      i = i - 1 # brings items from the unsorted sublist into the sorted sublist
  return A
