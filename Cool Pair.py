a = [4, 5, 6, 7, 8]
b = [8, 9, 10, 11, 12]
def coolPairs(a, b):
    uniqueSums = {k:v for k in a for v in b if (k*v) % (k+v)==0}
    print(uniqueSums)
    return len(uniqueSums)
print(coolPairs(a,b))