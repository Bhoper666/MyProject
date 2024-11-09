import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (320,240))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    dif = frame - bgr

    cv2.imshow('OG', frame)
    cv2.imshow('HSV', hsv)
    cv2.imshow('BGR', bgr)
    cv2.imshow('Difference', dif)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
