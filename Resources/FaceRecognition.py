import cv2
import face_recognition
import os
import pickle

class FaceRecognitionApp:
    def __init__(self):
        # Load the encoded face data from the pickle file
        with open("EncodedFile.p", "rb") as file:
            encodeListKnownWithIds = pickle.load(file)

        self.encodeListKnown, self.studentIds = encodeListKnownWithIds

        # Initialize the webcam
        self.cap = cv2.VideoCapture(0)

    def run(self):
        while True:
            ret, frame = self.cap.read()

            # Resize the frame for faster processing (optional)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Find face locations in the current frame
            face_locations = face_recognition.face_locations(frame)
            face_encodings = face_recognition.face_encodings(frame, face_locations)

            # Loop through the detected faces
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                # Compare the current face encoding with the stored encodings
                matches = face_recognition.compare_faces(self.encodeListKnown, face_encoding)
                name = "Unknown"  # Default name if no match is found

                # Check if there is a match
                if True in matches:
                    matched_index = matches.index(True)
                    name = self.studentIds[matched_index]

                # Draw a rectangle around the detected face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                # Display the name of the recognized person above the face
                cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

            # Display the frame with annotations
            frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
            cv2.imshow('Face Recognition', frame)

            # Press 'q' to exit the loop
            if cv2.waitKey(1) & 0xFF == ord("~"):
                break

        # Release the webcam and close all windows
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    app = FaceRecognitionApp()
    app.run()
