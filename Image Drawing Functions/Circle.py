import cv2

image = cv2.imread("C:\\Users\\shive\\Downloads\\Bin1.jpg")

if image is None:
    print("Error: Image not found or unable to load.")

else:
    print("Image loaded successfully.")

    center = (250, 250)
    radius = 150
    color = (0, 0, 255)  
    thickness = 5 # -1 for filled circle

    cv2.circle(image, center, radius, color, thickness)

    cv2.imshow("Circle Image", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
