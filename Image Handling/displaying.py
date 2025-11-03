import cv2

image = cv2.imread("C:\\Users\\shive\\Downloads\\Bin1.jpg")
 
if image is not None:
    cv2.imshow("Image showing", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not load image.")
    