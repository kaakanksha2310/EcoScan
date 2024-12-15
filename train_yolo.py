from ultralytics import YOLO

# Load the YOLOv8 model (Nano version for faster training)
model = YOLO("yolov8n.pt")  # Pre-trained Nano model

# Train the model on your dataset
model.train(data="/Users/aakankshakumari/Desktop/UnderaterFish/dataset.yaml", epochs=10, imgsz=640)

# Evaluate the model on the validation set
metrics = model.val()

# Export the trained model to ONNX or TorchScript if needed
model.export(format="onnx")
