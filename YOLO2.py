import cv2
import torch
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    anzahl_autos = 0
    bus_erkannt = False

    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])  
            if cls == 2: 
                anzahl_autos += 1
                print("Auto erkannt")
            elif cls == 5: 
                bus_erkannt = True

   
    with open("verkehrsdaten.txt", "w") as f:
        print(f"Writing data: {anzahl_autos},{int(bus_erkannt)}")  # Debugging line
        f.write(f"{anzahl_autos},{int(bus_erkannt)}")


cap.release()
cv2.destroyAllWindows()
