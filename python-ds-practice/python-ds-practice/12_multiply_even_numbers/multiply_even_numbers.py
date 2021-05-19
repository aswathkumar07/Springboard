def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    even_nos = [num for num in nums if num % 2 == 0]

    def product(args):
        prod = 1
        for a in args:
            prod *= a
        return prod
    answer = product(even_nos)
    return answer

print(multiply_even_numbers([2,4,6469]))