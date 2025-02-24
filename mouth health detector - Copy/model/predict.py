# model/predict.py
import cv2
import joblib
from utils.preprocess import load_images_from_folder

def predict(image_path):
    model = joblib.load('model/svm_model.joblib')
    img = cv2.imread(image_path)
    img = cv2.resize(img, (64, 64)).flatten()
    prediction = model.predict([img])
    return prediction[0]
