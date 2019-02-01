
data = {
    "A" : [
        [9, -9, -4,  3,  6],
        [7, -3, -8,  4,  4],
        [7, -9,  1, -2,  8],
        [5, -3, -4, -9, -8],
        [8,  5, -5,  4,  6]
    ],

    "B" : [
        [ 2, -7,  2, -2,  0],
        [ 1,  8,  2,  2, -2],
        [ 6, -2,  5, -2,  5],
        [-4,  9, -5, -9, -7],
        [ 8,  0, -9,  2, -7]
    ],

    "C" : [
        [-9,  5, -1,  9,  4],
        [ 3, -4, -6, -3,  3],
        [ 6,  6,  7, -3, -6],
        [-8,  9,  6, -1, -2],
        [-10, 2, -8, -4,  9]
    ]
}

sum = { 'A': 0, 'B': 0, 'C': 0 }

for i in range(5):
    sum['A'] += data['A'][i][i] + data['A'][i][4-i]
    sum['B'] += data['B'][i][i] + data['B'][i][4-i]
    sum['C'] += data['C'][i][i] + data['C'][i][4-i]

for i in sum:
    print( 'Sum(' + i + ') = ' + str(sum[i]) )
    
smallest = 'A'

if ( sum[smallest] > sum['B'] ):
    smallest = 'B'
if ( sum[smallest] > sum['C'] ):
    smallest = 'C'

print( 'Smallest set: ' + smallest + ', sum = ' + str(sum[smallest]) )