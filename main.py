import pygame

class JeuDelaVie:
    def initializeFlags(self):
        self.leftTopCorner = False
        self.rightTopCorner = False
        self.bottomLeftCorner = False
        self.bottomRightCorner = False
        self.leftEdge = False
        self.topEdge = False
        self.rightEdge = False
        self.bottomEdge = False
        self.inTheMiddle = False

    def __init__(self, s):
        self.isblue = True
        self.x = 30
        self.y = 30
        self.color = (0, 128, 255)
        self.clock = pygame.time.Clock()
        self.screen = s

        # Create a 20 by 20 matrix
        self.size = 50
        self.board = [[0 for i in range(self.size)] for j in range(self.size)]

        # Blinker
        # self.board[1][2] = 1
        # self.board[2][2] = 1
        # self.board[3][2] = 1

        ''' Toad
        self.board[1][2] = 1
        self.board[1][3] = 1
        self.board[1][4] = 1
        self.board[2][1] = 1
        self.board[2][2] = 1
        self.board[2][3] = 1
        '''

        # Beacon
        # self.board[1][2] = 1
        # self.board[1][3] = 1
        # self.board[2][2] = 1
        # self.board[2][3] = 1
        # self.board[3][4] = 1
        # self.board[3][5] = 1
        # self.board[4][4] = 1
        # self.board[4][5] = 1

        # Pulsar
        self.board[1][3] = 1
        self.board[1][4] = 1
        self.board[1][5] = 1
        self.board[1][9] = 1
        self.board[1][10] = 1
        self.board[1][11] = 1
        self.board[6][3] = 1
        self.board[6][4] = 1
        self.board[6][5] = 1
        self.board[6][9] = 1
        self.board[6][10] = 1
        self.board[6][11] = 1
        self.board[8][3] = 1
        self.board[8][4] = 1
        self.board[8][5] = 1
        self.board[8][9] = 1
        self.board[8][10] = 1
        self.board[8][11] = 1
        self.board[13][3] = 1
        self.board[13][4] = 1
        self.board[13][5] = 1
        self.board[13][9] = 1
        self.board[13][10] = 1
        self.board[13][11] = 1
        self.board[3][1] = 1
        self.board[4][1] = 1
        self.board[5][1] = 1
        self.board[3][6] = 1
        self.board[4][6] = 1
        self.board[5][6] = 1
        self.board[3][8] = 1
        self.board[4][8] = 1
        self.board[5][8] = 1
        self.board[3][13] = 1
        self.board[4][13] = 1
        self.board[5][13] = 1
        self.board[9][1] = 1
        self.board[10][1] = 1
        self.board[11][1] = 1
        self.board[9][6] = 1
        self.board[10][6] = 1
        self.board[11][6] = 1
        self.board[9][8] = 1
        self.board[10][8] = 1
        self.board[11][8] = 1
        self.board[9][13] = 1
        self.board[10][13] = 1
        self.board[11][13] = 1


        ''' Glider
        self.board[9][13] = 1;
        self.board[9][14] = 1;
        self.board[9][15] = 1;
        self.board[8][15] = 1;
        self.board[7][14] = 1;
        '''

        self.generation = 0
        self.initializeFlags()


    def analyzePoint(self, i, j):
        self.initializeFlags()
        max = self.size - 1
        self.leftTopCorner = (i == 0 and j == 0)
        if (self.leftTopCorner): return
        self.rightTopCorner = (i == 0 and j == max);
        if (self.rightTopCorner): return
        self.bottomLeftCorner = (i == max and j == 0)
        if (self.bottomLeftCorner): return
        self.bottomRightCorner = (i == max and j == max)
        if (self.bottomRightCorner): return
        self.leftEdge = (j == 0)
        if (self.leftEdge): return
        self.topEdge = (i == 0)
        if (self.topEdge): return
        self.rightEdge = (j == max)
        if (self.rightEdge): return
        self.bottomEdge = (i == max)
        if (self.bottomEdge): return
        self.inTheMiddle = True

    def getLeftTop(self, i, j):
        max = self.size - 1
        if (self.leftTopCorner): return self.board[max][max]
        if (self.rightTopCorner):  return self.board[max][j-1]
        if (self.bottomLeftCorner):  return self.board[i-1][max]
        if (self.bottomRightCorner):  return self.board[i-1][j-1]
        if (self.leftEdge):  return self.board[i-1][max]
        if (self.topEdge):  return self.board[max][j-1]
        if (self.rightEdge):  return self.board[i-1][j-1]
        if (self.bottomEdge):  return self.board[i-1][j-1]
        if (self.inTheMiddle):  return self.board[i-1][j-1]
        return 0

    def getTop(self, i, j):
        max = self.size - 1
        if (self.leftTopCorner): return self.board[max][j]
        if (self.rightTopCorner): return self.board[max][max]
        if (self.bottomLeftCorner): return self.board[i-1][j]
        if (self.bottomRightCorner): return self.board[i-1][j]
        if (self.leftEdge): return self.board[i-1][j]
        if (self.topEdge): return self.board[max][j]
        if (self.rightEdge): return self.board[i-1][j]
        if (self.bottomEdge): return self.board[i-1][j]
        if (self.inTheMiddle): return self.board[i-1][j]
        return 0

    def getRightTop(self, i, j):
        max = self.size - 1
        if (self.leftTopCorner): return self.board[max][j + 1]
        if (self.rightTopCorner): return self.board[max][0]
        if (self.bottomLeftCorner): return self.board[i-1][j+1]
        if (self.bottomRightCorner): return self.board[i-1][0]
        if (self.leftEdge): return self.board[i-1][j+1]
        if (self.topEdge): return self.board[max][j+1]
        if (self.rightEdge): return self.board[i-1][0]
        if (self.bottomEdge): return self.board[i-1][j+1]
        if (self.inTheMiddle): return self.board[i-1][j+1]
        return 0

    def getLeft(self, i, j):
        max = self.size - 1
        if (self.leftTopCorner): return self.board[i][max]
        if (self.rightTopCorner): return self.board[i][j-1]
        if (self.bottomLeftCorner): return self.board[max][max]
        if (self.bottomRightCorner): return self.board[max][j-1]
        if (self.leftEdge): return self.board[i][max]
        if (self.topEdge): return self.board[i][j-1]
        if (self.rightEdge): return self.board[i][j-1]
        if (self.bottomEdge): return self.board[i][j-1]
        if (self.inTheMiddle): return self.board[i][j-1]
        return 0

    def getRight(self, i, j):
        if (self.leftTopCorner): return self.board[i][j + 1]
        if (self.rightTopCorner): return self.board[i][0]
        if (self.bottomLeftCorner): return self.board[i][j+1]
        if (self.bottomRightCorner): return self.board[i][0]
        if (self.leftEdge): return self.board[i][j+1]
        if (self.topEdge): return self.board[i][j+1]
        if (self.rightEdge): return self.board[i][0]
        if (self.bottomEdge): return self.board[i][j+1]
        if (self.inTheMiddle): return self.board[i][j+1]
        return 0

    def getLeftBottom(self, i, j):
        max = self.size - 1
        if (self.leftTopCorner): return self.board[i + 1][max]
        if (self.rightTopCorner): return self.board[i+1][j-1]
        if (self.bottomLeftCorner): return self.board[0][max]
        if (self.bottomRightCorner): return self.board[0][max]
        if (self.leftEdge): return self.board[i+1][max]
        if (self.topEdge): return self.board[i+1][j-1]
        if (self.rightEdge): return self.board[i+1][j-1]
        if (self.bottomEdge): return self.board[0][j-1]
        if (self.inTheMiddle): return self.board[i+1][j-1]
   
        return 0

    def getBottom(self, i, j):
        if (self.leftTopCorner): return self.board[i+1][j]
        if (self.rightTopCorner): return self.board[i+1][j]
        if (self.bottomLeftCorner): return self.board[0][j]
        if (self.bottomRightCorner): return self.board[0][j]
        if (self.leftEdge): return self.board[i+1][j]
        if (self.topEdge): return self.board[i+1][j]
        if (self.rightEdge): return self.board[i+1][j]
        if (self.bottomEdge): return self.board[0][j]
        if (self.inTheMiddle): return self.board[i+1][j]
        return 0

    def getRightBottom(self, i, j):
        if (self.leftTopCorner): return self.board[i+1][j+1]
        if (self.rightTopCorner): return self.board[i+1][0]
        if (self.bottomLeftCorner): return self.board[0][j+1]
        if (self.bottomRightCorner): return self.board[0][0]
        if (self.leftEdge): return self.board[i+1][j+1]
        if (self.topEdge): return self.board[i+1][j+1]
        if (self.rightEdge): return self.board[i+1][0]
        if (self.bottomEdge): return self.board[0][j+1]
        if (self.inTheMiddle): return self.board[i+1][j+1]
        return 0

    def sum(self, i, j):
        leftTop = self.getLeftTop(i, j)
        top = self.getTop(i, j)
        rightTop = self.getRightTop(i, j)
        left = self.getLeft(i, j)
        right = self.getRight(i, j)
        leftBottom = self.getLeftBottom(i, j)
        bottom = self.getBottom(i, j)
        rightBottom = self.getRightBottom(i, j)
        return leftTop + top + rightTop + \
               left + 0 + right + \
               leftBottom + bottom + rightBottom

    def setConfiguration(self, board):
        for row in range(self.size):
            for col in range(self.size):
                self.board[row][col] = board[row][col]

    def nextConfiguration(self):
        board = [[0 for i in range(self.size)] for j in range(self.size)]

        for row in range(self.size):
            for col in range(self.size):
                self.analyzePoint(row, col)
                sum = self.sum(row, col);
                alive = self.board[row][col] == 1

                # Any live cell with fewer than two live neighbours dies,
                # as if caused by underpopulation.
                if (alive and sum < 2):
                    board[row][col] = 0

                # Any live cell with two or three live neighbours
                # lives on to the next generation.
                if (alive and sum == 2 or
                    alive and sum == 3):
                    board[row][col] = 1

                # Any live cell with more than three live neighbours dies,
                # as if by overpopulation.
                if (alive and sum > 3):
                    board[row][col] = 0

                # Any dead cell with exactly three live neighbours becomes a live cell,
                # as if by reproduction.
                if (not alive and sum == 3):
                    board[row][col] = 1



        # Apply to main board
        self.setConfiguration(board)


    # Display the current board
    def displayBoard(self, x, y, color):
        for row in range(self.size):
            for col in range(self.size):
                if (self.board[row][col] == 1):
                    #rect = pygame.Rect(x+(row*20), y+(col*20), 10, 10)
                    pygame.draw.circle(self.screen, color, (x+(row*20), y+(col*20)), 20, 1)



# Entry point

pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Le Jeu De La Vie")
jeu = JeuDelaVie(screen)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            jeu.isblue = not jeu.isblue
        if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
            jeu.nextConfiguration()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: jeu.y -= 3
    if pressed[pygame.K_DOWN]: jeu.y += 3
    if pressed[pygame.K_LEFT]: jeu.x -= 3
    if pressed[pygame.K_RIGHT]: jeu.x += 3

    # Add this somewhere after the event pumping and before the display.flip()
    rect = pygame.Rect(jeu.x, jeu.y, 60, 60)
    if jeu.isblue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)

    jeu.screen.fill((0, 0, 0))
    jeu.displayBoard(10, 10, color)

    pygame.display.flip()
    jeu.clock.tick(60)

    pygame.time.wait(1000)
    jeu.nextConfiguration()


