from roboflow import Roboflow
rf = Roboflow(api_key="Q9IcsfJCMLzQzVoymuKT")
project = rf.workspace().project("smartbinwaste")
model = project.version(2).model

# infer on a local image
print(model.predict("image.jpg", confidence=60, overlap=30).json())

# visualize your prediction
# model.predict("your_image.jpg", confidence=40, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())
