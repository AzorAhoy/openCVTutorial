import cv2
import numpy as np

img = cv2.imread('sudoku.png',0)
_, th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

cv2.imshow("image",img)
cv2.imshow("TH1",th1)


cv2.waitKey()
cv2.destroyAllWindows()