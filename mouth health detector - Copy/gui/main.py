import sys
import os
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.predict import predict

def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        img = img.resize((250, 250), Image.LANCZOS)  # Updated to Image.LANCZOS
        img = ImageTk.PhotoImage(img)
        panel.configure(image=img)
        panel.image = img

        result = predict(file_path)
        result_text.set(f"Prediction: {'Inflamed' if result == 1 else 'Healthy'}")

root = tk.Tk()
root.title("Mouth Health Detector")

panel = tk.Label(root)
panel.pack()

btn_upload = tk.Button(root, text="Upload Image", command=upload_image)
btn_upload.pack()

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.pack()

root.mainloop()
