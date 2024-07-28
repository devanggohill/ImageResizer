import cv2

# Path to the input image
input_image_path = 'devang.jpg'

# Path to save the resized image
output_image_path = 'resized_image.jpg'

# Read the image from file
image = cv2.imread(input_image_path)

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load image.")
else:
    # Resize the image to new dimensions (width, height)
    new_width = 600
    new_height = 400
    resized_image = cv2.resize(image, (new_width, new_height))

    # Save the resized image to a file
    cv2.imwrite(output_image_path, resized_image)

    # Display the original and resized images
    cv2.imshow('Original Image', image)
    cv2.imshow('Resized Image', resized_image)

    # Wait indefinitely until a key is pressed
    cv2.waitKey(0)

    # Destroy all OpenCV windows
    cv2.destroyAllWindows()
