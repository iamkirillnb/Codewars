def solution(s):
    a = []
    if len(s) % 2 == 0:
        for i in range(1, int(len(s)), 2):
            a.append(s[i-1:i+1])
    else:
        s = s + '_'
        for i in range(1, int(len(s)), 2):
            a.append(s[i-1:i+1])
    return a

# print(solution('asdfgh'))
# print(solution('asdfg'))