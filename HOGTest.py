# import cv2
# hog = cv2.HOGDescriptor()
# hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
# 
# def detector(image):
#    rects, weights = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8),scale=1.05)
#    for (x, y, w, h) in rects:
#        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
#        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
#    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
#    result = non_max_suppression(rects, probs=None, overlapThresh=0.7)
#    return result
# 
# frame = cv2.imread("/.../pedestrian2.jpg")
# result = detector(frame.copy())
# for (xA, yA, xB, yB) in result:     # draw the final bounding boxes after non-maxima supression
#     cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)
# img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# img_out = PIL.Image.fromarray(img)
# img_out