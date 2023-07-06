import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255

# canvas tuvali, baslangic, bitis, renk, kalinlik
cv2.line(canvas, (50, 50), (512, 512), (255, 0, 0), thickness=5)
cv2.line(canvas, (100, 50), (200, 250), (0, 0, 255), thickness=7)

# canvas tuvali, sol ust kose, sag alt kose,
# -1 degeri icini doldurur
cv2.rectangle(canvas, (20, 20), (50, 50), (0, 255, 0), thickness=-1)
cv2.rectangle(canvas, (50, 50), (150, 150), (0, 255, 0), thickness=-1)

# canvas tuvali, merkez, yaricap, renk, kalinlik
cv2.circle(canvas, (250, 250), 100, (0, 0, 255), thickness=-1)

# triangle
p1 = (100, 200)
p2 = (50, 50)
p3 = (300, 100)

cv2.line(canvas, p1, p2, (0, 0, 0), 4)
cv2.line(canvas, p2, p3, (0, 0, 0), 4)
cv2.line(canvas, p1, p3, (0, 0, 0), 4)

# random line
points = np.array([[[110, 200], [330, 200], [290, 220], [100, 100]]], np.int32)

# canvas tuvali, pointler, kapali olmasi icin True, renk, kalinlik
cv2.polylines(canvas, [points], True, (0, 0, 100), 5)

# canvas tuvali, merkez noktasi, genislik yukseklik, yatay aci, baslangic, bitis derecesi , renk, kalinlik
cv2.ellipse(canvas, (300, 300), (100, 50), 0, 0, 360, (255, 255, 0), -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
