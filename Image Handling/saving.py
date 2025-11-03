import cv2

image = cv2.imread("C:\\Users\\shive\\Downloads\\Bin1.jpg")
 
if image is not None:
    success = cv2.imwrite("C:\\Users\\shive\\Downloads\\Bin1_copy.jpg", image)
    if success:
        print("Image saved successfully as 'Bin1_copy.jpg'")
    else:
        print("Error: Unable to save the image.")
else:
    print("Error: Image not found or unable to load.")
    