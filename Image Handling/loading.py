import cv2

image = cv2.imread("C:\\Users\\shive\\Downloads\\Bin1.jpg")
 
if image is None:
    print("Error: Image not found or unable to load.")
else:
    print("Image loaded successfully.")
    