import cv2
import time
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

phone_start_time = None
last_drink_time = time.time()
person_missing_time = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose=False)[0]

    person_detected = False
    phone_detected = False
    drink_detected = False

    for box in results.boxes:
        cls = int(box.cls[0])

        if cls == 0:
            person_detected = True
        if cls == 67:
            phone_detected = True
        if cls == 39 or cls == 41:
            drink_detected = True

    current_time = time.time()

    if not person_detected:
        if person_missing_time is None:
            person_missing_time = current_time
    else:
        person_missing_time = None

    if phone_detected:
        if phone_start_time is None:
            phone_start_time = current_time
    else:
        phone_start_time = None

    if drink_detected:
        last_drink_time = current_time

    status = "Idle"
    color = (255,255,255)

    if person_missing_time and current_time - person_missing_time > 5:
        status = "System Paused: User Away"
        color = (0,255,255)

    elif phone_start_time and current_time - phone_start_time > 2:
        status = "WARNING: PUT PHONE AWAY"
        color = (0,0,255)

    elif current_time - last_drink_time > 30:
        status = "HEALTH ALERT: Drink Water"
        color = (255,0,0)

    elif person_detected:
        status = "Status: Focusing"
        color = (0,255,0)

    cv2.putText(frame, status, (20,60), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

    for box in results.boxes:
        x1,y1,x2,y2 = map(int, box.xyxy[0])
        cls = int(box.cls[0])

        if cls in [0,39,41,67]:
            if cls == 67:
                c = (0,0,255)
            else:
                c = (0,255,0)

            cv2.rectangle(frame,(x1,y1),(x2,y2),c,2)

    cv2.imshow("AuraGuard", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()