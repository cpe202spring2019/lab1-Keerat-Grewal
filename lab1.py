
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
    pass


def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    count = len(int_list) - 1
    if int_list is None:
        raise ValueError
    if count == 0:
        return []
    return reverse_rec(int_list[count - 1]) + int_list[count]
    pass


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    pass
