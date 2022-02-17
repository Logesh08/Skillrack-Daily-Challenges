# Smallest Submatrix - Min and Max Integers
# The program must accept an integer matrix of size R*C containing only unique integers as the input. The program must print the smallest possible submatrix having the minimum integer and the maximum integer in the matrix.

# Boundary Condition(s):
# 2 <= R, C <= 50
# 1 <= Matrix element value <= 10^4

# Input Format:
# The first line contains R and C separated by a space.
# The next R lines, each contains C integer values separated by a space.

# Output Format:
# The lines contain the smallest possible submatrix having the minimum integer and the maximum integer in the matrix.

# Example Input/Output 1:
# Input:
# 5 6
# 73 31 19 10 27 12
# 82 66 15 23 64 89
# 17 40 74 41 99 38
# 46 79 91 28 57 35
# 94 97 45 55 33 56

# Output:
# 10 27
# 23 64
# 41 99

# Explanation:
# The minimum integer in the matrix is 10.
# The maximum integer in the matrix is 99.
# So the smallest submatrix with 10 and 99 is given below.
# 10 27
# 23 64
# 41 99

# Example Input/Output 2:
# Input:
# 8 7
# 556 808 424 922 560 423 973
# 219 146 679 906 444 474 185
# 664 409 294 472 884 377 508
# 166 386 703 133 768 390 919
# 715 538 861 840 110 378 102
# 798 981 130 759 860 769 277
# 463 940 328 942 313 623 151
# 514 450 779 883 764 157 733

# Output:
# 538 861 840 110 378 102
# 981 130 759 860 769 277











r,c=map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(r)]
hig=low=mat[0][0]
a=b=x=y=0
for i in range(r):
    for j in range(c):
        val = mat[i][j]
        if val>hig:
            hig=val
            a=i;b=j
        if val<low:
            low=val
            x=i;y=j
si = min([a,x])
sj = min([b,y])
ei = max([a,x])
ej = max([b,y])
for i in range(si,ei+1):
    for j in range(sj,ej+1):
        print(mat[i][j],end=' ')
    print()


