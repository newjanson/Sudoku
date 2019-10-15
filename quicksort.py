from partition import partition


def quicksort(a: list, l: int, u: int):
  """
  Sort the given list a in non-descending order.
  Precondition: 0 <= l and u < len(a)
  >>> a = [1,2,3]
  >>> quicksort(a, 0, 2)
  >>> a
  [1, 2, 3]
  """
  if l < u:
    pivot = a[u]
    i = partition(a, l, u-1, pivot)
    a[i], a[u] = a[u], a[i]
    quicksort(a, l, i-1)
    quicksort(a, i+1, u)
