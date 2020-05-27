def mutate_string(string, position, character):
    s_new = list(s)
    s_new[int(i)] = c
    s_new = ''.join(s_new)
    return s_new

s = input()
i, c = input().split()
print(i,c)
s_new = mutate_string(s, int(i), c)
print(s_new)
