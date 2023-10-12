import tkinter as tk
from FaceRecognition import FaceRecognitionApp


class GUIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition GUI")

        # Create a button to start the face recognition
        self.start_button = tk.Button(root, text="Start Face Recognition", command=self.start_face_recognition)
        self.start_button.pack(padx=10, pady=10)

    def start_face_recognition(self):
        # Create an instance of the FaceRecognitionApp class and run it
        face_recognition_app = FaceRecognitionApp()
        face_recognition_app.run()

if __name__ == "__main__":
    root = tk.Tk()
    app = GUIApp(root)
    root.mainloop()
