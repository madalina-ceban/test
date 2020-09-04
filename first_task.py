def LPS (x, i, j):
    if i == j:
        return 1 
    if i>j:
        return 0
    if x[i] == x[j]:
        #verificam in interior, largim 
        return LPS(x, i+1, j-1) + 2
    return max(LPS(x, i+1, j), LPS(x, i, j-1))


x = input("Ia sa vedem: ")
n = len(x);

print(LPS(x, 0, n-1));
