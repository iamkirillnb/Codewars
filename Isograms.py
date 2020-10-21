def is_isogram(string):
    string = list(map(str, string.lower()))
    mas = set(string)
    return len(string) == len(mas)

