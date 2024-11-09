import cv2

record = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 30.0, (1280,720))

while True:
    ret, frame = record.read()
    out.write(frame)
    cv2.imshow('Recorder window ^_^', frame)
    if cv2.waitKey(1) == ord('q'):
        break

record.release()
out.release()
cv2.destroyAllWIndows()
