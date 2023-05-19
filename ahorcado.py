board = [" -----", "     |", "     |", "     |", "     |", "     |", "------" ]
pasos = (("|",1,1), ("o",1,2), ("\\",0,2), ("/",2,2),("|",1,3),("/",0,4),("\\",2,4))

def drawboard():
    for i in board:
        print(i)

def testboard():
    for paso in pasos:
        caracter = paso[0]
        x = paso[1]
        y = paso[2]
        print (caracter, x, y)

drawboard()
testboard()