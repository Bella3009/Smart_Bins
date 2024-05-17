import cv2
from roboflow import Roboflow
rf = Roboflow(api_key="P8s0kpMADt2zWD7STKh3")
project = rf.workspace().project("smartrecycling")
model = project.version(1).model

imgPath = "Image/"

def captureImage():
    #This is the function that takes care of capturing the image
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
        return False, None

def itemIdentification():
    # This function takes care of recognising the item in the image
    while True:
        result, img = captureImage()
        if result:
            # data is transformed to a dictionary to better retrieve the information
            data = model.predict(img, confidence=50, overlap=30).json()

            predictions = data['predictions']
            for prediction in predictions:
                confidence = prediction['confidence']
                confidence = confidence * 100
                object = prediction['class']
            
                if confidence >= 50:
                    print("Class: " + object)
                    print("Confidence: " + str(confidence))
                    return object
                else:
                    print("Image captured show "+ object + " with " + str(confidence) + "% Image to be taken again")

if __name__ == '__main__':

    try:
        obj = itemIdentification()
        print(obj)
    except KeyboardInterrupt:
        print("Ending program")