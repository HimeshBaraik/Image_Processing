import cv2 as cv
import numpy as np

def dot_display(N):

    #Intialise with blank display
    blank = np.zeros((300, 500), dtype=np.uint8) 
    
    N = str(N)
    N = N[4:6]
    

    #parameter initialize 
    w = 50
    r = 25 

    #storing each digit in a dictionary
    dotdigit = {}
    
    dotdigit['0'] = [[1,1,1],[1,0,1],[1,0,1],[1,0,1],[1,1,1]]
    dotdigit['1'] = [[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0]]
    dotdigit['2'] = [[1,1,1],[0,0,1],[1,1,1],[1,0,0],[1,1,1]]
    dotdigit['3'] = [[1,1,1],[0,0,1],[1,1,1],[0,0,1],[1,1,1]]
    dotdigit['4'] = [[1,0,1],[1,0,1],[1,1,1],[0,0,1],[0,0,1]]
    dotdigit['5'] = [[1,1,1],[1,0,0],[1,1,1],[0,0,1],[1,1,1]]
    dotdigit['6'] = [[1,1,1],[1,0,0],[1,1,1],[1,0,1],[1,1,1]]
    dotdigit['7'] = [[1,1,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1]]
    dotdigit['8'] = [[1,1,1],[1,0,1],[1,1,1],[1,0,1],[1,1,1]]
    dotdigit['9'] = [[1,1,1],[1,0,1],[1,1,1],[0,0,1],[1,1,1]]


    # drawing each dot one by one on the blank image
    x = 0
    for num in N:
        dig = dotdigit[num]
        for i in range(5):
            for j in range(3):
                if dig[i][j]:
                    centre = (x + 5 + 10*(j) + r + 2*r*j, 5 + 10*(i) + r + 2*r*i)
                    blank = cv.circle(blank, centre , r, (255) ,-1)
        x += 180 + w

    return blank

N = input("Enter 6 digit number")
img = dot_display(N)
cv.imshow("dotted",img)
cv.waitKey(0)
