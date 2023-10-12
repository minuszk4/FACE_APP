import os
import cv2
import tkinter as tk
from tkinter import ttk, filedialog
from tkinter.simpledialog import askstring
from PIL import Image, ImageTk
from encoding_generator import FaceRecognitionSystem
Step1 = True
StepOpen = False
StepCam = False

class CameraApp:
    def __init__(self, root):
        global StepCam, Step1, StepOpen
        self.root = root
        self.root.title("Camera App")
        self.face_recognition_system = FaceRecognitionSystem("F:\Project\Face Recognition\Images")
        # Initialize flags
        self.camera_mode = True

        # Create a label for displaying images
        self.label = ttk.Label(root)
        self.label.pack(padx=10, pady=10)

        # Initialize save_button attribute as None
        self.save_button = None

        # Create buttons for actions
        if Step1:
            self.open_camera_button = ttk.Button(root, text="Open Camera", command=self.toggle_camera)
            self.open_camera_button.pack()
            self.open_file_button = ttk.Button(root, text="Open File", command=self.open)
            self.open_file_button.pack()

        # Create an Exit button
        self.exit_button = ttk.Button(root, text="Exit", command=self.exit_app)
        self.exit_button.pack()

        # Initialize camera capture
        self.cap = cv2.VideoCapture(0)

    def toggle_camera(self):
        global StepCam, Step1
        StepCam = True
        Step1 = False
        self.cap = cv2.VideoCapture(0)
        self.update_camera()
        # Create the "Save Image" button
        if not self.save_button:
            self.save_button = ttk.Button(self.root, text="Save Image", command=self.save_image)
            self.save_button.pack()

    def update_camera(self):
        global StepCam
        if StepCam:
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img)
                self.label.config(image=imgtk)
                self.label.imgtk = imgtk
                self.label.photo = imgtk
                self.label.after(10, self.update_camera)
            else:
                print("Unable to read from the camera.")
                self.root.quit()

    def save_image(self):
        global StepCam
        if StepCam:
            ret, frame = self.cap.read()
            if ret:
                filename = askstring("Enter the name for the image:", "Name:")
                if filename:
                    current_directory = "F:\Project\Face Recognition"
                    filepath = os.path.join(current_directory, "Images", f"{filename}.png")
                    cv2.imwrite(filepath, frame)
                    print("Camera image saved successfully.")
                    self.label.config(text="Saved: " + filepath)
            else:
                print("Unable to save the camera image.")
                self.label.config(text="Error saving camera image.")
        else:
            imgtk = self.label.imgtk
            if imgtk:
                filename = askstring("Enter the name for the image:", "Name:")
                if filename:
                    current_directory = os.getcwd()
                    filepath = os.path.join(current_directory, "Images", f"{filename}.png")
                    img = imgtk.image
                    img.save(filepath)
                    print("Image opened from file saved successfully.")
                    self.label.config(text="Saved: " + filepath)
        folder_path = r"F:\Project\Face Recognition\Images"
        output_file = "EncodedFile.p"

        face_recognition_system = FaceRecognitionSystem(folder_path)
        face_recognition_system.load_images()
        face_recognition_system.encode_images()
        face_recognition_system.save_encoded_data(output_file)


    def open(self):
        global StepOpen, StepCam, Step1
        StepOpen = True
        StepCam = False
        Step1 = False
        filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if filepath:
            img = Image.open(filepath)

            # Resize the image to your desired dimensions (e.g., 640x480)
            img = img.resize((640, 480), Image.LANCZOS)  # Use Image.ANTIALIAS for anti-aliasing

            imgtk = ImageTk.PhotoImage(image=img)
            self.label.config(image=imgtk)
            self.label.imgtk = imgtk
            # Hide the Exit and Save buttons when opening a file
            self.exit_button.pack_forget()
            if not self.save_button:
                self.save_button = ttk.Button(self.root, text="Save Image", command=self.save_image)
                self.save_button.pack()
        else:
            print("No file selected")

    def exit_app(self):
        global Step1, StepOpen, StepCam
        if Step1:
            self.root.quit()
        else:
            Step1 = True
            StepOpen = False
            StepCam = False
            self.label.config(image=None)
            self.label.imgtk=None
            self.label.photo=None
            self.camera_mode = True
            self.open_camera_button.config(state=tk.NORMAL)
            self.cap.release()
            self.open_file_button.config(state=tk.NORMAL)
            if self.save_button:
                self.save_button.destroy()  # Destroy the "Save Image" button if it exists

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = CameraApp(root)
    app.root.protocol("WM_DELETE_WINDOW", app.exit_app)  # Handle window close button
    app.run()
