import cv2

# Replace the below URL with your stream URL
stream_url = 'udp://@:1234'  # This is the address where the stream is received.

# Use OpenCV to capture the video stream
cap = cv2.VideoCapture(stream_url)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Failed to retrieve frame. Exiting...")
        break

    # Display the resulting frame
    cv2.imshow('Video Stream', frame)

    # Press 'q' on the keyboard to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
