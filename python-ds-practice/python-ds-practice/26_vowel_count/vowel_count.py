from collections import Counter
def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = {}
    for vowel in phrase.lower():
        if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u':
            if vowel not in vowels:
                vowels[vowel] = 1
            else:
                vowels[vowel] += 1
    return vowels

print(vowel_count('rithm school'))
print(vowel_count('HOW ARE YOU? i am great!') )