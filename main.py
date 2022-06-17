import cv2
camera_id = 0
cap = cv2.VideoCapture(camera_id)
while (cap.isOpened()):
    #đọc ảnh
    ret, frame = cap.read()
    #hiển ảnh
    cv2.imshow("cam",frame)
    #kiểm tra nếu bấm q thì break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#giải phóng camera
cap.release()
cv2.destroyAllWindows()