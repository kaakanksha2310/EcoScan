from ultralytics import YOLO
import cv2

# Load the trained model
model = YOLO("detect/train2/weights/best.pt")  # Path to the correct model weights

# Path to a test image
image_path = "data/test/images/sample2.jpg"  # Replace with your actual test image path

# Perform inference
results = model.predict(image_path, save=True, conf=0.5)  # Perform inference and save annotated results

# Display the saved annotated image
annotated_image_path = "detect/predict/sample.jpg"  # Path to the saved annotated image
image = cv2.imread(annotated_image_path)
cv2.imshow("Detection Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
