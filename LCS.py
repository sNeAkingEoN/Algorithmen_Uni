import sys

eins_str = sys.argv[1]
zwei_str = sys.argv[2]
eins = list(eins_str)
zwei = list(zwei_str)
eins_laen = len(eins)
zwei_laen = len(zwei)
matrix = [[0]*(len(zwei)+1) for x in range(0,len(eins)+1)]
# Achtung! Die Matrix baut es andersrum auf als ich gemacht hätte
print('matrix:', matrix)
lcs_count = 0 # int
lcs_lit = '' # string

def matrix_to_string(ma):
    for m in ma:
        print(m)

for i, e in enumerate(eins):
    for j, z in enumerate(zwei):
        if e == z:
            print('found', 'lcs_count:', lcs_count, 'eins:', e, 'an Stelle', i, 'zwei:', z, 'an Stelle', j, '!\n')
            # hier geht's weiter <3
            matrix[i+1][j+1] = matrix[i][j] + 1
        else:
            if matrix[i][j+1] >= matrix[i+1][j]:
                matrix[i+1][j+1] = matrix[i][j+1]
            else:
                matrix[i+1][j+1] = matrix[i+1][j]


print('Longest common subsequence:', lcs_count)
print(matrix_to_string(matrix))
