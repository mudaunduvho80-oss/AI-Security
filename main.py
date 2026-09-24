import cv2

from detector import detect_person
from config import CAMERA_INDEX, WINDOW_NAME
from alert import send_alert


print("================================")
print("     AI SECURITY SYSTEM")
print("================================")
print("Starting system...")


# Start the camera
camera = cv2.VideoCapture(CAMERA_INDEX)

if not camera.isOpened():
    print("ERROR: Could not open camera.")
    exit()


print("Camera started successfully.")
print("System is now monitoring...")
print("Press Q to stop.")
print("--------------------------------")


# Remember the previous detection state
person_was_detected = False


# Keep the security system running
while True:

    # Capture a frame
    success, frame = camera.read()

    if not success:
        print("ERROR: Could not read camera frame.")
        break


    # Detect a person
    person_detected, results = detect_person(frame)


    # Person has just appeared
    if person_detected and not person_was_detected:
        send_alert()


    # Person has just left
    if not person_detected and person_was_detected:
        print("PERSON LEFT!")


    # Remember current detection state
    person_was_detected = person_detected


    # Draw detection boxes
    annotated_frame = results[0].plot()


    # Display camera
    cv2.imshow(WINDOW_NAME, annotated_frame)


    # Press Q to stop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# Close everything
camera.release()
cv2.destroyAllWindows()


print("--------------------------------")
print("AI Security System stopped.")