from ultralytics import YOLO

# Load the best-trained model
model = YOLO("runs/detect/train/weights/best.pt")

# Evaluate the model on the validation set
metrics = model.val()
print(metrics)
