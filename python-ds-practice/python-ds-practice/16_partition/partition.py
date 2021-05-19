def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """
    boolean_map =  map(fn,lst)
    true_lst = []
    false_lst = []
    merged_lst = []

    boolean_lst = list(boolean_map)
    for index, x in enumerate(boolean_lst):
        if x == True:
            true_lst.append(lst[index])
    for index_2, x_2 in enumerate(boolean_lst):
        if x_2 == False:
            false_lst.append(lst[index_2])

    return [true_lst, false_lst]

def is_even(num):
    return num % 2 == 0

def is_string(el):
    return isinstance(el, str)

print(partition([1, 2, 3, 4], is_even))
print(partition(["hi", None, 6, "bye"], is_string))
