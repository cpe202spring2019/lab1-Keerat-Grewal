
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError
    elif len(int_list) == 0:
        return None
    int_max = int_list[0]
    for i in int_list:
        if i > int_max:
            int_max = i
    return int_max


def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError
    if len(int_list) == 0:
        return []
    if len(int_list) == 1:
        return int_list[0:]
    return reverse_rec(int_list[1:len(int_list)]) + int_list[0:1]


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    if int_list is None:
        raise ValueError
    if len(int_list) == 0:
        return None
    mid = (low + high) // 2
    if low > high:
        return None
    elif int_list[mid] == target:
        return mid
    elif int_list[mid] < target:
        low = mid + 1
        return bin_search(target, low, high, int_list)
    else:
        high = mid - 1
        return bin_search(target, low, high, int_list)

