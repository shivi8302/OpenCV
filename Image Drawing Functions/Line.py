import cv2

image = cv2.imread("C:\\Users\\shive\\Downloads\\Bin1.jpg")

if image is None:
    print("Error: Image not found or unable to load.")

else:
    print("Image loaded successfully.")

    pt1 = (100, 200)
    pt2 = (400, 200)
    color = (0, 255, 0)  
    thickness = 5

    cv2.line(image, pt1, pt2, color, thickness)

    cv2.imshow("Line Image", image)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
