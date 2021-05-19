def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    s = list(s)
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    vowels_in_word = []
    for i in s:
        if i in vowels:
            vowels_in_word.append(i)
    vowels_in_word.reverse()

    index = 0
    for k in range(len(s)-1):
        if s[k] in vowels:
            s[k] = vowels_in_word[index]
            index += 1

    final_string = ''
    for ele in s:
        final_string += ele
    return final_string

print(reverse_vowels("Hello!"))
print(reverse_vowels("Tomatoes"))
print(reverse_vowels("Reverse Vowels In A String"))
print(reverse_vowels("aeiou"))
print(reverse_vowels("why try, shy fly?"))


