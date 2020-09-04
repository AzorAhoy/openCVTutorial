import cv2

img = cv2.imread('lena.jpg', 0) & 0xFF

print(img)

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