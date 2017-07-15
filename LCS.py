import sys

eins_str = sys.argv[1]
zwei_str = sys.argv[2]
#eins = list(eins_str) # vgl. main-Methode
#zwei = list(zwei_str)
#eins_laen = len(eins) # noch nie benutzt
#zwei_laen = len(zwei)
#erzeuge Matrix:
#matr = [[0]*(len(zwei)+1) for x in range(0,len(eins)+1)]
# Achtung! Die Matrix baut es andersrum auf als ich gemacht hätte,
# ist aber egal, da es letztendlich um den Weg geht
# print('matrix:', matr) # weiß ich jetzt, dass das klappt :)
lcs_count = 0 # int
lcs_lit = '' # string

def print_matrix(ma):
    for m in ma:
        print(m)

def fill_matrix(matrix, eins, zwei):
    for i, e in enumerate(eins):
        for j, z in enumerate(zwei):
            if e == z:
                matrix[i+1][j+1] = matrix[i][j] + 1
            else:
                if matrix[i][j+1] >= matrix[i+1][j]:
                    matrix[i+1][j+1] = matrix[i][j+1]
                else:
                    matrix[i+1][j+1] = matrix[i+1][j]
    lcs_count = matrix[-1][-1]
    return matrix



#matrix = fill_matrix(matr) # da es nichts returnt, scheint es direkt von einer Klassenvariable auszugehen?
# macht es auch, wenn es das returnt!


#rücke Indizes an Stelle von letztem Feld:
#i = len(matrix) - 1 # in Fkt. verbacken :)
#j = len(matrix[i]) - 1
'''
weiteres Vorgehen
Lege fest, wie viel noch gefunden werden muss:
chars_left = lcs_count
LCS = ''
# left-first:
gucke nach links. Wenn links gleich, dann gehe nach links
                Wenn links kleiner, dann gucke nach oben

gucke nach oben. Wenn oben gleich, dann gehe nach oben
                Wenn oben kleiner, dann JUMP

JUMP: speichere aktuelle Stelle im Outstring *vor* dem Rest
    gehe eins nach oben *und* eins nach links

definieren: JUMP
'''
# jetzt wird das ausgecodet:

def build_str_left_first(matrix, eins, zwei): # eins und zwei sind strings oder Arrays, müsste egel sein. wwwwoow.
    i = len(matrix) - 1
    print("i:", i)
    j = len(matrix[i]) - 1
    print("j:", j)
    chars_left = matrix[-1][-1] # zähle, wie viele Zeichen noch gesucht werden
    print("Zu findende Zeichen:", chars_left)
    LCS = '' #outstring
    while chars_left:
        if matrix[i][j-1] == matrix[i][j]:
            print('nach links gehen')
            j = j - 1 # nach links gehen
            continue
        elif matrix[i-1][j] == matrix[i][j]: # nach oben gucken
            print('nach oben gehen')
            i = i - 1# nach oben gehen
            continue
        else:
            print('jump')
            LCS = eins[i-1] + LCS # oder zwei[j-1] # JUMP
            chars_left -= 1 # Änderung 3. Sitzung! While-loop muss terminieren!
            i = i - 1
            j = j - 1
            continue
    return LCS



def main(str1, str2):
    eins = list(str1)
    zwei = list(str2)
    matrix = [[0]*(len(zwei)+1) for x in range(0,len(eins)+1)]
    fill_matrix(matrix, eins, zwei)
    print_matrix(matrix)
    lcs_count = matrix[-1][-1]
    outstring = build_str_left_first(matrix, eins, zwei)
    print('Longest common subsequence:', lcs_count)
    return outstring



result = main(eins_str, zwei_str)
# print('Longest common subsequence:', lcs_count)
#print("Matrix:")
# print_matrix(matrix)
print("LCS: " + result)
