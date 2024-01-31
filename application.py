import face_recognition
import cv2
import csv
from datetime import datetime

# Replace these with the paths to your images and corresponding names
known_face_images = [
    "./public/images/faces/parth.jpg",
    "./public/images/faces/sankalp.jpg",
]
known_face_names = ["Parth", "Sankalp"]

# Load the known faces and names
known_faces = [face_recognition.load_image_file(img) for img in known_face_images]
known_encodings = [face_recognition.face_encodings(face)[0] for face in known_faces]

# Open the camera
video_capture = cv2.VideoCapture(0)

# Set a higher frame width and height for better performance
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Open a CSV file for writing recognized names
csv_file_path = "recognized_names.csv"
with open(csv_file_path, mode="w", newline="") as csv_file:
    fieldnames = ["Timestamp", "RecognizedName"]
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    while True:
        # Capture every frame
        ret, frame = video_capture.read()

        # Find face locations and face encodings in the current frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        # Loop through each face found in the frame
        for (top, right, bottom, left), face_encoding in zip(
            face_locations, face_encodings
        ):
            # Check if the face matches any known faces
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            name = "Unknown"

            # If a match is found, use the name of the known face
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

                # Get the current date and time
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Write recognized names and timestamp to CSV file
                csv_writer.writerow({"Timestamp": timestamp, "RecognizedName": name})

            # Draw a rectangle around the face and display the name
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(
                frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1
            )

        # Display the resulting frame
        cv2.imshow("Video", frame)

        # Adjust the waitKey parameter for better FPS
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

# Release the camera, close all windows, and close the CSV file
video_capture.release()
cv2.destroyAllWindows()
