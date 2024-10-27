import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk, ImageEnhance
import cv2
import numpy as np

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", ".jpg;.jpeg;*.png")])
    if file_path:
        global original_image, displayed_image
        original_image = Image.open(file_path)
        displayed_image = original_image.copy()
        update_image_display(displayed_image)

def save_image():
    if displayed_image:
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", ".png"), ("JPEG files", ".jpg"), ("All Files", ".")])
        if file_path:
            displayed_image.save(file_path)
            messagebox.showinfo("Image Saved", "Image has been saved successfully!")

def update_image_display(img):
    img_tk = ImageTk.PhotoImage(img)
    canvas.image = img_tk
    canvas.create_image(0, 0, anchor="nw", image=img_tk)

def apply_filter(filter_type):
    global displayed_image
    if original_image:
        if filter_type == "Grayscale":
            displayed_image = original_image.convert("L")
        elif filter_type == "Contrast":
            enhancer = ImageEnhance.Contrast(original_image)
            displayed_image = enhancer.enhance(1.5)
        elif filter_type == "Edge Detection":
            gray_image = np.array(original_image.convert("L"))
            edges = cv2.Canny(gray_image, 100, 200)
            displayed_image = Image.fromarray(edges)
        elif filter_type == "Cartoon":
            img_np = np.array(original_image)
            gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
            gray = cv2.medianBlur(gray, 5)
            edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
            color = cv2.bilateralFilter(img_np, 9, 250, 250)
            cartoon = cv2.bitwise_and(color, color, mask=edges)
            displayed_image = Image.fromarray(cartoon)
        update_image_display(displayed_image)

# Initialize main window
root = tk.Tk()
root.title("AI Photo Editor")
root.geometry("800x600")

# Canvas for image display
canvas = tk.Canvas(root, width=500, height=400, bg="gray")
canvas.pack(pady=20)

# Control buttons
frame = tk.Frame(root)
frame.pack()

btn_open = tk.Button(frame, text="Open Image", command=open_image)
btn_open.grid(row=0, column=0, padx=10, pady=10)

btn_save = tk.Button(frame, text="Save Image", command=save_image)
btn_save.grid(row=0, column=1, padx=10, pady=10)

# Filter options
filter_frame = tk.LabelFrame(root, text="Filters")
filter_frame.pack(pady=20)

filters = ["None", "Grayscale", "Contrast", "Edge Detection", "Cartoon"]
for i, filter_type in enumerate(filters):
    btn = tk.Button(filter_frame, text=filter_type, command=lambda f=filter_type: apply_filter(f))
    btn.grid(row=0, column=i, padx=10, pady=5)

# Main loop
original_image = None
displayed_image = None
root.mainloop()
