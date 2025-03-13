import cv2
import numpy as np

net = cv2.dnn.readNetFromCaffe("/home/raspberry/path/to/deploy.prototxt","/home/raspberry/path/to/mobilenet_iter_73000.caffemodel")
nap = cv2.VideoCapture(0)

while True:
    ret,farme=cap.read()
    if not ret:
        break 

    h,w =frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame,0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detection=net.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0,0,i,2]
        if confidence > 0.5:
            box = detctions[0,0,i,3:7] * np.array([w,h,w,h])
            (startX, startY, endX, endY) = box.astype("int")
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0,255,0), 2)

    cv2.imshow("Frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()