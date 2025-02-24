import sys
import os
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.predict import predict

def upload_image():
    global file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            img = Image.open(file_path)
            img = img.resize((300, 300), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            panel.configure(image=img)
            panel.image = img
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

def analyze_image():
    if file_path:
        try:
            result = predict(file_path)
            result_text.set(f"Prediction: {'Inflamed' if result == 1 else 'Healthy'}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

root = tk.Tk()
root.title("Mouth Health Detector")
root.geometry("450x600")
root.resizable(False, False)

style = ttk.Style(root)
style.configure("TButton", font=("Helvetica", 12))
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TFrame", padding=10)
style.configure("TFrame.TFrame", borderwidth=2, relief="solid")

main_frame = ttk.Frame(root, style="TFrame")
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

upload_frame = ttk.LabelFrame(main_frame, text="Upload Section", padding="10")
upload_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

analyze_frame = ttk.LabelFrame(main_frame, text="Analyze Section", padding="10")
analyze_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

panel = ttk.Label(upload_frame)
panel.pack(pady=10)

btn_upload = ttk.Button(upload_frame, text="Upload Image", command=upload_image)
btn_upload.pack(pady=10)

btn_analyze = ttk.Button(analyze_frame, text="Analyze Image", command=analyze_image)
btn_analyze.pack(pady=10)

result_text = tk.StringVar()
result_label = ttk.Label(analyze_frame, textvariable=result_text, font=("Helvetica", 16))
result_label.pack(pady=10)

root.mainloop()
