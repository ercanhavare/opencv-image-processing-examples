import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

file_name = "C:/Users/ercan/PycharmProjects/udemyOpenCv/video_save/webcam.avi"
# fourcc sitesinden video uzantisina gore c1,c2,c3,c4 degeri degisiklik gosterebilir
codec = cv2.VideoWriter_fourcc('W', 'M', 'V', '2')

frame_rate = 30
resolution = (640, 480)

video_file_output = cv2.VideoWriter(file_name, codec, frame_rate, resolution)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # y eksenine gore yansimasi, 0 ve -1 farkli yansimalar icin girilebilir
    video_file_output.write(frame)
    cv2.imshow("Webcam Live", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_file_output.release()
cap.release()
cv2.destroyAllWindows()
