def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    list_word = [ltr for ltr in phrase]
    dict_letter_count = {}
    for ltr in list_word:
        if ltr not in dict_letter_count.keys():
            dict_letter_count[ltr] = 1
        else:
            dict_letter_count[ltr] += 1
    return dict_letter_count

print(multiple_letter_count('yay'))
print(multiple_letter_count('Yay'))