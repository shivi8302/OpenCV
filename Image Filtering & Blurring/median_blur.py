import cv2

image = cv2.imread('C:\\Users\\shive\\Downloads\\Bin1.jpg')

blurred_image = cv2.medianBlur(image, 5)

cv2.imshow('Median Blurred Image', blurred_image)
cv2.waitKey(0)      
cv2.destroyAllWindows() 

