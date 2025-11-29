import cv2

image = cv2.imread("C:\\Users\\shive\\Downloads\\Bin1.jpg")

if image is None:
    print("Error: Image not found or unable to load.")

else:
    print("Image loaded successfully.")

    cv2.putText(image, "Hello Programmers" ,(560,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)

    cv2.imshow("Text Image", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
