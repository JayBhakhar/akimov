import cv2
import numpy as np

# todo: import weight() 
# https://drive.google.com/file/d/1IBZjePdAWq7LtEG3qu_EDMNg4hF44mPI/view?usp=sharing
cv = cv2.dnn.readNet("items_weights.weights","config.cfg")
classes = []

with open("item_list.txt", "r") as file:
    classes = [line.strip() for line in file.readlines()]

layer_names = cv.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in cv.getUnconnectedOutLayers()]

colorRed = (0,0,255)
colorGreen = (0,255,0)

# todo: Load Image
name = "D:\semeter 5\_akimov\photo.jpg"
img = cv2.imread(name)
height, width, channels = img.shape

# # Detecting objects
blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

cv.setInput(blob)
outputs = cv.forward(output_layers)

class_ids = []
confidences = []
boxes = []
for output in outputs:
    for detection in output:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
for i in range(len(boxes)):
    if i in indexes:
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        cv2.rectangle(img, (x, y), (x + w, y + h), colorGreen, 3)
        cv2.putText(img, label, (x, y + 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, colorRed, 4)



img = cv2.imwrite("output1.jpg",img)
cv2.imshow("Image", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()