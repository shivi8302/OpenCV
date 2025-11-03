import cv2

image = cv2.imread("C:\\Users\\shive\\Downloads\\Bin1.jpg")
 
if image is not None:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Image showing", gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not load image.")
    