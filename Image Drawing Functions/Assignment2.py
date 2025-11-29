import cv2

file = input("Enter the path to the image file: ")
image = cv2.imread(file)

if image is not None:
    task = input("Enter the task you want to perform (circle, line, rectangle, text): ").strip().lower()

    if task == "circle":

        x = int(input("Enter the x coordinate of the circle center:"))
        y = int(input("Enter the y coordinate of the circle center:"))
        radius = int(input("Enter the radius of the circle:"))
        color = (255,255,255)  # Default color is pink
        thickness = int(input("Enter the thickness of the circle border (-1 for filled):"))
        cv2.circle(image, (x, y), radius, color, thickness)
    
        cv2.imshow("Image with Circle", image)
        cv2.waitKey(0)  
        cv2.destroyAllWindows()
        print("Circle drawn successfully.")

        save_response = input("Do you want to save the modified image? (yes/no):").strip().lower()

        if save_response == "yes":
            save_path = input("Enter the path to save the modified image (including filename and extension):")
            cv2.imwrite(save_path, image)
            print(f"Image saved successfully at {save_path}.")
    
        else:
            print("Image not saved.")

    elif task == "line":
        x = int(input("Enter the x coordinate of the starting point:"))
        y = int(input("Enter the y coordinate of the starting point:"))
        x2 = int(input("Enter the x coordinate of the ending point:"))
        y2 = int(input("Enter the y coordinate of the ending point:"))
        color = (255,255,255)
        thickness = int(input("Enter the thickness of the line:"))
        cv2.line(image, (x, y), (x2, y2), color, thickness)
    
        cv2.imshow("Image with Line", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Line drawn successfully.")

        save_response = input("Do you want to save the modified image? (yes/no):").strip().lower()

        if save_response == "yes":
            save_path = input("Enter the path to save the modified image (including filename and extension):")
            cv2.imwrite(save_path, image)
            print(f"Image saved successfully at {save_path}.")
    
        else:
            print("Image not saved.")

    elif task == "rectangle":
        x = int(input("Enter the x coordinate of the top-left corner:"))
        y = int(input("Enter the y coordinate of the top-left corner:"))
        x2 = int(input("Enter the x coordinate of the bottom-right corner:"))
        y2 = int(input("Enter the y coordinate of the bottom-right corner:"))
        color = (255,255,255)
        thickness = int(input("Enter the thickness of the rectangle border (-1 for filled):"))
        cv2.rectangle(image, (x, y), (x2, y2), color, thickness)
    
        cv2.imshow("Image with Rectangle", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Rectangle drawn successfully.")

        save_response = input("Do you want to save the modified image? (yes/no):").strip().lower()

        if save_response == "yes":
            save_path = input("Enter the path to save the modified image (including filename and extension):")
            cv2.imwrite(save_path, image)
            print(f"Image saved successfully at {save_path}.")
    
        else:
            print("Image not saved.")

    elif task == "text":
        x = int(input("Enter the x coordinate of the bottom-left corner of the text:"))
        y = int(input("Enter the y coordinate of the bottom-left corner of the text:"))
        text = input("Enter the text to be drawn:")
        font_scale = float(input("Enter the font scale (e.g., 1.0):"))
        color = (255,255,255)
        thickness = int(input("Enter the thickness of the text:"))
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, text, (x, y), font, font_scale, color, thickness)
    
        cv2.imshow("Image with Text", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Text drawn successfully.")

        save_response = input("Do you want to save the modified image? (yes/no):").strip().lower()

        if save_response == "yes":
            save_path = input("Enter the path to save the modified image (including filename and extension):")
            cv2.imwrite(save_path, image)
            print(f"Image saved successfully at {save_path}.")
    
        else:
            print("Image not saved.")

    else:
        print("Invalid task. Please choose from circle, line, rectangle, or text.")

else:
    print("Error: Could not load the image. Please check the file path and try again.")
    