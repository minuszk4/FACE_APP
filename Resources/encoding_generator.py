import os
import cv2
import pickle
import face_recognition

class FaceRecognitionSystem:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.imgs_list = []
        self.name_list = []
        self.encoded_list = []

    def load_images(self):
        folder = os.listdir(self.folder_path)
        for i in folder:
            img = cv2.imread(os.path.join(self.folder_path, i))
            if img is not None:
                self.imgs_list.append(img)
                self.name_list.append(os.path.splitext(i)[0])

    def encode_images(self):
        for img in self.imgs_list:
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img_rgb)[0]
            self.encoded_list.append(encode)

    def save_encoded_data(self, output_file):
        encoded_list_name = [self.encoded_list, self.name_list]
        with open(output_file, "wb") as file:
            pickle.dump(encoded_list_name, file)

if __name__ == "__main__":
    folder_path = r"F:\Project\Face Recognition\Images"
    output_file = "EncodedFile.p"

    face_recognition_system = FaceRecognitionSystem(folder_path)
    face_recognition_system.load_images()
    face_recognition_system.encode_images()
    face_recognition_system.save_encoded_data(output_file)
