import cv2 

image_path = input("Enter the image path:")
image1 = cv2.imread(image_path)
if image1 is not None:
    gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    task = input("Enter the task (show/save): ").strip().lower()

    if task == "show":
        h = 1000
        w = 1000
        c = 3
        image = cv2.resize(gray, (w, h))
        h,w,c = image.shape
        print(f"Height: {h}\nWidth: {w}\nChannels: {c}")
        cv2.imshow("Grayscale Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    elif task == "save":
        save_path = input("Enter the path to save the grayscale image: ")
        success = cv2.imwrite(save_path, gray)
        if success:
            print(f"Image saved successfully at {save_path}")
        else:
            print("Error: Unable to save the image.")
else:
    print("Error: Could not load image.")



