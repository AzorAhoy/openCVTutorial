import cv2

img = cv2.imread('lena.jpg', 1) & 0xFF

print(img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('image', img)
k = cv2.waitKey(0)
# cv2.destroyAllWindows()
if k == 27:
    cv2.destroyAllWindows()
    print("Success!")
elif k == ord('s'):
    cv2.destroyAllWindows()
    cv2.imwrite('lena_copy.png', img)
    print("Success!")