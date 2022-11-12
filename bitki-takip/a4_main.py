import cv2
import a4_utils

###################################
webcam = True
path = "image.jpg"
cap = cv2.VideoCapture("http://192.168.43.150:8080")
cap.set(10, 160)
cap.set(3, 1920)
cap.set(4, 1080)
scale = 2
wP = 2231 * scale
hP = 3999 * scale
###################################

while True:
    if webcam:
        success, img = cap.read()
    else:
        img = cv2.imread(path)

    imgContours, conts = a4_utils.getContours(img, minArea=50000, filter=4)
    if len(conts) != 0:
        biggest = conts[0][2]
        # print(biggest)
        imgWarp = a4_utils.warpImg(img, biggest, wP, hP)
        imgContours2, conts2 = a4_utils.getContours(imgWarp,
                                                    minArea=2000, filter=4,
                                                    cThr=[50, 50], draw=False)
        if len(conts) != 0:
            for obj in conts2:
                cv2.polylines(imgContours2, [obj[2]], True, (0, 255, 0), 2)
                nPoints = a4_utils.reorder(obj[2])
                nW = round(
                    (a4_utils.findDis(nPoints[0][0]//scale, nPoints[1][0]//scale)/10), 1)
                nH = round(
                    (a4_utils.findDis(nPoints[0][0]//scale, nPoints[2][0]//scale)/10), 1)
                cv2.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[1][0][0], nPoints[1][0][1]),
                                (255, 0, 255), 3, 8, 0, 0.05)
                cv2.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[2][0][0], nPoints[2][0][1]),
                                (255, 0, 255), 3, 8, 0, 0.05)
                x, y, w, h = obj[3]
                cv2.putText(imgContours2, "{}cm".format(nW), (x + 30, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5,
                            (255, 0, 255), 2)
                cv2.putText(imgContours2, "{}cm".format(nH), (x - 70, y + h // 2), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5,
                            (255, 0, 255), 2)
        cv2.imshow("A4", imgContours2)

    img = cv2.resize(img, (0, 0), None, 0.5, 0.5)
    cv2.namedWindow("Original", cv2.WINDOW_KEEPRATIO)
    cv2.imshow("Original", img)
    cv2.waitKey(0)
