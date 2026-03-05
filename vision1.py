import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
BOTTLE_CLASS_ID = 39

def open_camera(indices=(0, 1, 2, 3)):
    for idx in indices:
        cap = cv2.VideoCapture(idx, cv2.CAP_V4L2)
        if cap.isOpened():
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
            print(f"Using camera index: {idx}")
            return cap
        cap.release()
    return None

cap = open_camera()

if cap is None:
    print("Error: Cannot access any camera. Check /dev/video* and camera permissions.")
    exit()

print("Bottle Detection Started... Press 'q' to quit.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    result = model.predict(
        source=frame,
        classes=[BOTTLE_CLASS_ID],
        conf=0.35,
        imgsz=640,
        verbose=False,
    )[0]

    for box in result.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(
            frame,
            "Bottle Detected",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2,
        )

    cv2.imshow("Bottle Detector - Computer Vision", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

