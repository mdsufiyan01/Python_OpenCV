# import cv2 library (computer vision v2)
import cv2


img = cv2.imread('mera.png', 0) # image.png (full name of the image to be viewed)

print(img)  # (it will print array values of image in output terminal)

# frame-name  (sets window's name of the image viewer)
cv2.imshow("frame-name", img)

# waitkey stop the window for the given specific time (1000 = 1 sec)
cv2.waitKey(5000)

# .destroyAllWindows closes the window ie: (frame-name)
cv2.destroyAllWindows()
