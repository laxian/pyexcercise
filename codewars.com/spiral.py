
# https://www.codewars.com/kata/534e01fbbb17187c7e0000c6

def spiralize(size):
    if size==1:
        return [[1]]
    elif size==2:
        return [[1,0],[0,0]]
    spiral = [[0 for x in range(0, size)] for y in range(0, size)]

    row,col=0,0
    ords = ['r', 'b', 'l', 'u']
    ord = 0
    while True:
        ori = ords[ord % 4]
        rowl=spiral[row]
        rowl[col]=1
        moved=0
        if ori == 'r':
            if 1 in rowl[col+1:]:
                while col<size-3 and rowl[col+1]==0 and rowl[col+2]==0:
                    col+=1
                    rowl[col]=1
                    moved+=1
            else:
                while col<size-1 and rowl[col+1]==0:
                    col+=1
                    rowl[col]=1
                    moved+=1

        elif ori == 'b':
            while row<size-3 and spiral[row+1][col]==0 and spiral[row+2][col]==0:
                row+=1
                spiral[row][col]=1
                moved+=1
            if spiral[row+1][col]==0 and spiral[row+2][col]==0:
                spiral[row+1][col]=1
                spiral[row+2][col]=1
                row+=2
                moved+=2

        elif ori == 'l':
            if 1 in rowl[:col]:
                while col>2 and rowl[col-1]==0 and rowl[col-2]==0:
                    col-=1
                    rowl[col]=1
                    moved+=1
            else:
                while col>0 and rowl[col-1]==0:
                    col-=1
                    rowl[col]=1
                    moved+=1
        elif ori == 'u':
            while row>2 and spiral[row-1][col]==0 and spiral[row-2][col]==0:
                row-=1
                spiral[row][col]=1
                moved+=1
            if spiral[row-1][col]==0 and spiral[row-2][col]==0:
                spiral[row-1][col]=1
                spiral[row-2][col]=1
                row-=2
                moved+=2

        if moved<2:
            break
        ord += 1

    return spiral

size=3
lst=spiralize(size)
for i in range(0,size):
    print(lst[i])