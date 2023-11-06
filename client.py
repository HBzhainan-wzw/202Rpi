import cv2
import socket
import numpy as np

# Set up the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind to any incoming data on this port
sock.bind(('0.0.0.0', 10001))

# Assuming a maximum packet size of 65507 bytes (though it might be less)
MAX_DGRAM_SIZE = 65507

try:
    # Loop to continuously receive data
    while True:
        # Receive data
        packet_data, addr = sock.recvfrom(MAX_DGRAM_SIZE)
        
        # Here, we directly decode each packet's data. In a real application, you would need
        # to handle packet reordering, and possibly reconstruct the frame from several packets
        # if your frame size exceeds the packet size.
        frame = np.frombuffer(packet_data, dtype=np.uint8)
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)

        # Check if frame is valid
        if frame is not None:
            cv2.imshow('Video Stream', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    sock.close()
    cv2.destroyAllWindows()
