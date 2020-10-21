def get_count(input_str):
    num_vowels = 0
    for i in input_str.replace(' ', '').lower():
        if i in ['a', 'i', 'e', 'o','u']:
            num_vowels += 1
    return num_vowels

#print(get_count('adasdad'))