def find_next_square(sq):
    number = sq**0.5
    if number.is_integer():
        number = (number+1)**2
        return number
    return -1

#print(find_next_square(144))