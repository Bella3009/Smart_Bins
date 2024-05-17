import cv2
from roboflow import Roboflow
rf = Roboflow(api_key="P8s0kpMADt2zWD7STKh3")
project = rf.workspace().project("smartrecycling")
model = project.version(1).model

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
        return True, image
    else:
        print("Failed to capture image.")
        return False

def itemIdentification():
    while True:
        result, img = captureImage()
        if result:
            data = model.predict(img, confidence=60, overlap=30).json()

            predictions = data['predictions']
            for prediction in predictions:
                confidence = prediction['confidence']
                object = prediction['class']
            
                if confidence >= 40:
                    print("Class: " + object)
                    print("Confidence: " + str(confidence * 100))
                    return object
                else:
                    print("Image captured show "+ object + " with " + str(confidence * 100) + "% Image to be taken again")

if __name__ == '__main__':
    print('Program is starting ... ')
    try:
        itemIdentification()
        
    except KeyboardInterrupt:
        print("Ending program")