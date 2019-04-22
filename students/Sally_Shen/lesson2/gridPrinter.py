
'''Printing a Grid'''


def grid(rowCols, dashes):
    edge = '+'
    row = '|'
    for i in range(rowCols):
        edge += '-' * dashes
        edge += '+'
        row += ' ' * dashes
        row += '|'
    edge += '\n'
    row += '\n'

    result = edge
    for i in range(rowCols):
        for j in range(dashes):
            result += row
        result += edge
    print(result)

grid(5, 3)

# grid(7,6,7)

#print('+', '-'*4,'+', '-'*4,'+')
#print('|',' '*4 , '|', ' '*4, '|')
#print('|',' '*4 , '|', ' '*4, '|')
#print('|',' '*4 , '|', ' '*4, '|')
#print('|',' '*4 , '|', ' '*4, '|')
#print('+', '-'*4,'+', '-'*4,'+')
#print('|',' '*4 , '|', ' '*4, '|')
#print('|',' '*4 , '|', ' '*4, '|')
#print('|',' '*4 , '|', ' '*4, '|')
#print('|',' '*4 , '|', ' '*4, '|')
#print('+', '-'*4,'+', '-'*4,'+')


