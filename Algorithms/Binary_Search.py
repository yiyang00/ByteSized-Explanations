# Binary Search 

def binary_search(A, item):
  begin = 0
  end = len(A) - 1 # since index of python starts at 0

  while begin <= end:
    mid = begin + (end - begin) // 2  # finding the index of the midpoint
    mid_value = A[mid]
    if mid_value == item: # if we find item
      return mid
    elif item < mid_value: # item is in the left of the mid_value
      end = mid - 1 # end point would now be the element 1 index to the left of the midpoint
    else: # item greater than midpoint --> value of item lies to the right of midpoint
      begin = mid + 1 # starting index would be the element 1 index to the right of the midpoint

  return None # if item not found
