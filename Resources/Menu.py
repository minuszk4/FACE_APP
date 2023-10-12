import tkinter as tk
from tkinter import ttk
from FaceRecGui import GUIApp
from SaveImageGui import CameraApp

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition App")

        # Create a button for "Nhận diện" (Face Recognition)
        self.face_recognition_button = ttk.Button(root, text="Nhận diện", command=self.open_face_recognition)
        self.face_recognition_button.pack(padx=10, pady=10)

        # Create a button for "Chụp ảnh" (Capture Photo)
        self.capture_photo_button = ttk.Button(root, text="Chụp ảnh", command=self.open_capture_photo)
        self.capture_photo_button.pack(padx=10, pady=10)

    def open_face_recognition(self):
        # Create a new window for Face Recognition
        new_window = CustomWindow(self.root, "Face Recognition")
        gui_app = GUIApp(new_window.window)  # Sử dụng .window để truy cập cửa sổ Toplevel

    def open_capture_photo(self):
        # Create a new window for Capture Photo
        new_window = CustomWindow(self.root, "Capture Photo")
        camera_app = CameraApp(new_window.window)  # Sử dụng .window để truy cập cửa sổ Toplevel

class CustomWindow:
    def __init__(self, master, title):
        self.master = master
        self.window = tk.Toplevel(master)
        self.window.title(title)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
