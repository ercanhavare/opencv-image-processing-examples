import cv2
import numpy as np

# + 255 canvasi beyaz yapiyor
canvas = np.zeros((512,512,3),dtype=np.uint8) + 255
#print(canvas)

cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

