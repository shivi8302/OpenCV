import cv2

image = cv2.imread("C:\\Users\\shive\\Downloads\\Bin1.jpg")
 
if image is not None:
    # h = 300
    # w = 400
    # image = cv2.resize(image, (w, h))
    h,w,c = image.shape
    print(f"Height: {h}\nWidth: {w}\nChannels: {c}")
    # cv2.imshow("Image", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
else:
    print("Error: Image not found or unable to load.")

