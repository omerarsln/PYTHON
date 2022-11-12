from imageai.Detection import ObjectDetection
import os
import cv2

pixelToCM = 45/512

Kamera = cv2.VideoCapture('http://192.168.43.1:8080/video')
execution_path = os.getcwd()
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join(
    execution_path, "resnet50_coco_best_v2.1.0.h5"))
detector.loadModel()

ret, kare = Kamera.read()
cv2.imwrite("image.jpg", kare)

detections = detector.detectObjectsFromImage(input_image=os.path.join(
    execution_path, "image.jpg"), output_image_path=os.path.join(execution_path, "imagenew.jpg"))

print(detections)
for eachObject in detections:
    print(eachObject["name"], " : ", eachObject["percentage_probability"])
    box_points = eachObject["box_points"]
    genislik = box_points[2] - box_points[0]
    uzunluk = box_points[3] - box_points[1]
    print(str(genislik) + "--" + str(uzunluk))

new_image = cv2.imread("imagenew.jpg")

cv2.namedWindow("Fotograf", cv2.WINDOW_KEEPRATIO)
cv2.imshow("Fotograf", new_image)
cv2.waitKey(0)
