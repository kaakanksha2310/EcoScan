import os

label_dir = "./data/train/labels"  # Adjust this path to the 'labels' folder
unique_classes = set()

# Iterate through all label files
for label_file in os.listdir(label_dir):
    if label_file.endswith(".txt"):
        with open(os.path.join(label_dir, label_file), "r") as file:
            for line in file:
                class_id = int(line.split()[0])  # Extract the class_id
                unique_classes.add(class_id)

print("Unique Classes Found:", unique_classes)
print("Number of Classes (nc):", len(unique_classes))
