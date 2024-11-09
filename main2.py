import cv2

img = cv2.imread('res/cat.png')
cv2.namedWindow('rotate90', cv2.WINDOW_NORMAL)
cv2.resizeWindow('rotate90', 200, 200)
cv2.namedWindow('rotate180', cv2.WINDOW_NORMAL)
cv2.resizeWindow('rotate180', 200, 200)
cv2.namedWindow('rotate270', cv2.WINDOW_NORMAL)
cv2.resizeWindow('rotate270', 200, 200)

img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('rotate90', img)
img = cv2.rotate(img, cv2.ROTATE_180)
cv2.imshow('rotate180', img)
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow('rotate270', img)


cv2.waitKey(0)
