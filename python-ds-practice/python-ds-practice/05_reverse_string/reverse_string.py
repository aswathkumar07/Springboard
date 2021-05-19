def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    letters = [letter for letter in phrase]
    letters.reverse()
    str_reversed = ""
    return str_reversed.join(letters)

print(reverse_string('awesome'))
print(reverse_string('sauce'))

