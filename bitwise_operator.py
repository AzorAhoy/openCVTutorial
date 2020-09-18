import cv2
import numpy as np

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)

img2 = np.full((250, 500, 3), 255, dtype=np.uint8)
img2 = cv2.rectangle(img2, (0, 0), (250, 250), (0, 0, 0), -1)
# img2 = np.hstack((np.zeros((500,250,1), dtype=np.uint8), np.ones((500,250,1), dtype=np.uint8)*255))

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
