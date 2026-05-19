def maxElement(arr):
  return max(arr)


def maxElement2(arr):
  m=0
  for i in arr:
    if i > m:
      m=i
  return m
