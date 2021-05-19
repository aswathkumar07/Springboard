def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    lst_phrase = list(phrase)
    for index, letter in enumerate(lst_phrase):
        if letter.lower() == to_swap.lower():
            if letter.islower():
                lst_phrase[index] = letter.upper()
            else:
                lst_phrase[index] = letter.lower()
    return ''.join(lst_phrase)

print(flip_case('Aaaahhh', 'a'))
