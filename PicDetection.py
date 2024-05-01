import cv2
from roboflow import Roboflow
rf = Roboflow(api_key="Q9IcsfJCMLzQzVoymuKT")
project = rf.workspace().project("smartbinwaste")
model = project.version(2).model

imgPath = "Image/"

def captureImage():
    camera = cv2.VideoCapture(0)
    print("Capturing image...")
    ret, frame = camera.read()  # Read a frame from the camera
    if ret:
        cv2.imwrite(imgPath+"image1.jpg", frame)  # Save the frame as an image
        print("Image captured successfully!")
        image = cv2.imread(imgPath+"image1.jpg")
        cv2.imwrite(imgPath+"image1.jpg", image)
    else:
        print("Failed to capture image.")

data = model.predict("Image/image1.jpg", confidence=20, overlap=30).json()

predictions = data['predictions']
for prediction in predictions:
    confidence = prediction['confidence']
    obj_class = prediction['class']
    print("Class: " + obj_class)
    print("Confidence: " + str(confidence * 100))