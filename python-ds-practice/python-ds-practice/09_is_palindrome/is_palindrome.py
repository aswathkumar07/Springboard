def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    lst_word = [letter for letter in phrase.lower().replace(" ","")]
    lst_word_reversed = lst_word[::-1]
    return lst_word_reversed == lst_word

print(is_palindrome("Malayalams"))

