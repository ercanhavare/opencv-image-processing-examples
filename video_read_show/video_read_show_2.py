import cv2

# 0 => external
# 1 => internal
cap = cv2.VideoCapture("volvo.mp4")

while True:
    ret, frame = cap.read()

    if ret == 0:
        break

    # aynada ki gibi gorunecek
    frame = cv2.flip(frame, 1)  # goruntuyu istediginiz eksene gore degistirir
    cv2.imshow("Volvo", frame)

    # her frame 1 ms gosterilecek
    if cv2.waitKey(20) & 0XFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
