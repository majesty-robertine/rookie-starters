import sys
import os
from tkinter import filedialog, messagebox
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.predict import predict

def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        img = img.resize((250, 250), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        panel.configure(image=img)
        panel.image = img

        result = predict(file_path)
        result_text.set(f"Prediction: {'Inflamed' if result == 1 else 'Healthy'}")

# Create the main window
root = tk.Tk()
root.title("Mouth Health Detector")
root.geometry("400x500")
root.configure(bg='white')

# Create a style
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), padding=10)
style.configure('TLabel', font=('Helvetica', 16))

# Create frames
header_frame = tk.Frame(root, bg='white')
header_frame.pack(pady=20)

button_frame = tk.Frame(root, bg='white')
button_frame.pack(pady=20)

image_frame = tk.Frame(root, bg='white')
image_frame.pack(pady=20)

# Add a header
header_label = ttk.Label(header_frame, text="Mouth Health Detector", font=("Helvetica", 20, "bold"), background='white')
header_label.pack()

# Add upload button
btn_upload = ttk.Button(button_frame, text="Upload Image", command=upload_image, style='TButton')
btn_upload.pack()

# Image panel
panel = tk.Label(image_frame, bg='white')
panel.pack()

# Add result label
result_text = tk.StringVar()
result_label = ttk.Label(image_frame, textvariable=result_text, style='TLabel', background='white')
result_label.pack(pady=20)

# Add a footer
footer_frame = tk.Frame(root, bg='white')
footer_frame.pack(side=tk.BOTTOM, pady=10)
footer_label = ttk.Label(footer_frame, text="Powered by AI", font=("Helvetica", 10), background='white')
footer_label.pack()

root.mainloop()
