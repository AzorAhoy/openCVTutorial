import cv2
import datetime

# cap = cv2.VideoCapture('vtest.avi')
cap = cv2.VideoCapture(0)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
print(height)
print(width)


cap.set(3, 1280)

cap.set(4, 1024)

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(cap.get(3))+' Height: ' + str(cap.get(4))
        dt = str(datetime.datetime.now())
        frame = cv2.putText(frame, dt, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(150) & 0xFF == ord('q'):
            break
    else:
        break


cap.release()
cv2.destroyAllWindows()