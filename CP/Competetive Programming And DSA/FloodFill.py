M = 8
N = 8
def floodfillUtil(screen, x, y, prevColor, newcolor):
    '''Utility Function For FloodFill'''
    if x < 0 or x >= N or y < 0 or y >= M or screen[x][y] != prevColor or screen[x][y] == newColor:
        return
    screen[x][y] = newColor
    floodfillUtil(screen, x+1, y, prevColor, newColor) #1
    floodfillUtil(screen, x, y+1, prevColor, newColor) #2
    floodfillUtil(screen, x-1, y, prevColor, newColor) #3
    floodfillUtil(screen, x, y-1, prevColor, newColor) #4
    floodfillUtil(screen, x+1, y+1, prevColor, newColor) #5
    floodfillUtil(screen, x-1, y-1, prevColor, newColor) #6
    floodfillUtil(screen, x+1, y-1, prevColor, newColor) #7
    floodfillUtil(screen, x-1, y+1, prevColor, newColor) #8





def floodfill(screen, x, y, newColor):
    '''FloodFill main function'''
    prevColor = screen[x][y]
    floodfillUtil(screen, x, y, prevColor, newColor)
    



screen = [[1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 0, 0],
          [1, 0, 0, 1, 1, 0, 1, 1],
          [1, 2, 2, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 2, 2, 0],
          [1, 1, 1, 1, 1, 2, 1, 1],
          [1, 1, 1, 1, 1, 2, 2, 1]]

x, y = 4, 4
newColor = 3
floodfill(screen, x, y, newColor)
for i in range(M):
    for j in range(N):
        print(screen[i][j], end = ' ')
    print()