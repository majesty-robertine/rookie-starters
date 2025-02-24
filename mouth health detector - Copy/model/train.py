# model/train.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import joblib
from utils.preprocess import load_images_from_folder

# Load data
healthy_images = load_images_from_folder('dataset/healthy')
inflamed_images = load_images_from_folder('dataset/inflamed')

# Create labels
healthy_labels = [0] * len(healthy_images)
inflamed_labels = [1] * len(inflamed_images)

# Combine data and labels
X = healthy_images + inflamed_images
y = healthy_labels + inflamed_labels

# Preprocess data
X = [cv2.resize(img, (64, 64)).flatten() for img in X]
X = np.array(X)
y = np.array(y)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = SVC(kernel='linear')
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'model/svm_model.joblib')

print("Model training complete.")
