import cv2


stream = cv2.VideoCapture(0)


while True:
    ret, frame = stream.read()

    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) == ord('p'):
        cv2.imwrite('first.png',frame)
    elif cv2.waitKey(1) == ord('q'):
        break
stream.release()
cv2.destroyAllWindows()

