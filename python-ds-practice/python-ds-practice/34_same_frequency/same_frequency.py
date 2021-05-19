from collections import Counter
def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    count_num1 = Counter(str(num1))
    count_num2 = Counter(str(num2))
    dict_num1 = dict(count_num1)
    dict_num2 = dict(count_num2)
    if dict_num1 == dict_num2:
        return True
    else:
        return False

print(same_frequency(551122,221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211))
