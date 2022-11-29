def binarysearch(arr, start, end, target):
    """
    :param arr: sorted array
    :param start: range
    :param end: range
    :param target: value want to find
    :return: index of value in arr
    """
    if start > end:
        raise IndexError
    left, right = start, end
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            return mid
    if arr[mid] != target:
        raise ValueError
    return mid


def lowerbound(arr, start, end, target):
    """
    :param arr: sorted array
    :param start: range
    :param end: range
    :param target: value want to find
    :return: index of value in arr
    """
    if start > end:
        raise IndexError
    left, right = start, end
    while left < right:
        mid = (left + right) // 2
        if target <= arr[mid]:
            right = mid
        else:
            left = mid + 1
    return left
def upperbound(arr, start, end, target):
    """
    :param arr: sorted array
    :param start: range
    :param end: range
    :param target: value want to find
    :return: index of value in arr
    """
    if start > end:
        raise IndexError
    left, right = start, end
    while left < right:
        mid = (left + right) // 2
        if target >= arr[mid]:
            left = mid + 1
        else:
            right = mid
    return left
