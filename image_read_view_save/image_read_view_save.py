import cv2

#img = cv2.imread("klon.jpg")

#gray
img = cv2.imread("klon.jpg",0)
#print(img)

#autosize window
cv2.namedWindow("image",cv2.WINDOW_NORMAL)

#window_name,image_variable
cv2.imshow("image",img)

cv2.imwrite("klon1.jpg",img)

cv2.waitKey(0)
cv2.destroyAllWindows()