import cv2

# 0 => external
# 1 => internal
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    # aynada ki gibi gorunecek
    frame = cv2.flip(frame, 1)  # goruntuyu istediginiz eksene gore degistirir
    cv2.imshow("Webcam", frame)

    # her frame 1 ms gosterilecek
    if cv2.waitKey(1) & 0XFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
