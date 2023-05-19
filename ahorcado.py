board = [" -----", "     |", "     |", "     |", "     |", "     |", "------" ]
pasos = (("|",1,1), ("o",1,2), ("\\",0,2), ("/",2,2),("|",1,3),("/",0,4),("\\",2,4))

def drawboard():
    """
    Dibuja el tablero
    """
    for i in board:
        print(i)

def drawpaso(numpaso):
    """
    Coloca en el tablero el paso indicado
    """
    paso = pasos[numpaso]
    caracter = paso[0]
    x = paso[1]
    y = paso[2]
    board[y] = board[y][:x] + caracter + board[y][x+1:]

def testboard():
    """
    Prueba el tablero completando los pasos del ahorcado
    """
    for numpaso in range(len(pasos)):
        drawpaso(numpaso)

drawboard()
testboard()
drawboard()