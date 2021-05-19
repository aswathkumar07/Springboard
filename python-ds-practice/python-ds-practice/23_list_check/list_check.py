def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    for x in lst:
        if type(x) != list:
            is_list = False
        else:
            is_list = True
    return is_list

print(list_check([[1], [2, 3]]))
print(list_check([[1], "nope"]))

