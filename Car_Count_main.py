import numpy as np
import pandas as pd
import cv2 
import cvzone
import os
from ultralytics import YOLO

# ----------------------------
# Check Dir
# ----------------------------
output_dir = r'.\detection'
output_file = os.path.join(output_dir, "hasil_car_counter.mp4")
model_dir = r'.\model'
os.makedirs(output_dir, exist_ok=True)
os.makedirs(model_dir, exist_ok=True)

# ----------------------------
# Define Model
# ----------------------------

model = YOLO(r".\model\yolov8n.pt")

# ----------------------------
# Read Video using CV2
# ----------------------------

mask = cv2.imread(r".\mask.png")
cap = cv2.VideoCapture(r".\source\cars.mp4")

# Save Video Configuration

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))



out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*"mp4v"), fps , (frame_width,frame_height))


car_count = 0
car_id_collection = []

if not cap.isOpened():
    print("video error")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if len(mask.shape) == 2:
        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    imgRegion = cv2.bitwise_and(frame, mask)
# Predict using YOLO, and annotate the frame
    results= model.track(imgRegion, classes=[2],tracker="bytetrack.yaml",persist=True)[0]


    limits = [200, 400, 673, 400]
    cv2.line(frame, (limits[0], limits[1]), (limits[2],limits[3]), (0,0,255) ,5)
            

    for box in results.boxes:
        if box.id is not None:
            car_id = int(box.id[0].cpu().numpy())
            x1,y1,x2,y2 = box.xyxy[0].cpu().numpy()
            cv2.rectangle(frame,(int(x1), int(y1)), (int(x2), int(y2)),(255, 0, 255), 3)

            cvzone.putTextRect(frame, f'ID: {car_id}', (int(x1), int(y1) - 10), 
                                        scale=1.5, thickness=2, offset=5)


            cx,cy,w,h = box.xywh[0].cpu().numpy()
            cx = int(cx)
            cy = int(cy)

            cv2.circle(frame,(cx,cy),5,(255,0,0), -1)

            if limits[0] < cx < limits[2] and limits[1] - 20 < cy < limits[3] + 20:
                if car_id not in car_id_collection:
                    car_id_collection.append(car_id)
                    car_count += 1
                    cv2.line(frame, (limits[0], limits[1]), (limits[2], limits[3]), (0, 255, 0), 5)
    
    cv2.putText(frame, f"Count : {car_count}", (50,100), cv2.FONT_HERSHEY_PLAIN, 5, (50, 50, 255), 8)
    out.write(frame)


    cv2.imshow("Video playback", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()