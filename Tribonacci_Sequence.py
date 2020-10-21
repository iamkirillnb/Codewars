def tribonacci(signature, n):
    if n == 0:
        return []
    if n < 3:
        return signature[0:n]
    lst = []
    lst.extend(signature)
    for i in range(n-3):
        lst.append(sum(lst[i:]))
    return lst

