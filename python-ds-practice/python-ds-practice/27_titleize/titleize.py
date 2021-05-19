def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    lst_words = phrase.split(' ')
    res_sentence = ''
    for word in lst_words:
        res_sentence = res_sentence + word[0].upper() + word[1:].lower() + ' '
    return res_sentence.strip()

print(titleize('this is awesome'))
print(titleize('oNLy cAPITALIZe fIRSt'))

