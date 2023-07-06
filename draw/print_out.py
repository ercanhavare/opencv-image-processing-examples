import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255

#canvas, metin, metin koordinati(x,y), yazi tipi, yazi buyuklugu, renk, yazi tipi

font1 = cv2.FONT_HERSHEY_SIMPLEX
font2 = cv2.FONT_HERSHEY_COMPLEX
font3 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

cv2.putText(canvas,"Oktay",(30,100),font3,2,(0,0,0),cv2.LINE_AA)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
