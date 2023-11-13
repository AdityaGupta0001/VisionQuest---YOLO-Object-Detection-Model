from ultralytics import YOLO
import cv2
def useImages(filePath):

    model = YOLO('../Yolo-Weights/yolov8n.pt')
    results = model(filePath, show=True)
    cv2.waitKey(0)