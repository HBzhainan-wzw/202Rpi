import subprocess
import shlex

# Function to build the ffmpeg command
def build_ffmpeg_command(input_device, framerate, video_size, output_address, output_port):
    command = f"ffmpeg -f v4l2 -framerate {framerate} -video_size {video_size} -i {input_device} " \
              f"-c:v libx264 -preset veryfast -maxrate 1000k -bufsize 2000k -f mpegts udp://{output_address}:{output_port}"
    return command

# Replace these values with your configuration
input_device = '/dev/video0'      # Your camera device path
framerate = '25'                  # Frames per second
video_size = '640x480'            # Video resolution
output_address = '192.168.1.100'  # IP address of the destination computer
output_port = '1234'              # Port number for the stream

# Build the ffmpeg command
ffmpeg_command = build_ffmpeg_command(input_device, framerate, video_size, output_address, output_port)

# Execute the command
process = subprocess.Popen(shlex.split(ffmpeg_command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print("Streaming started...")

# Wait for the process to complete
try:
    stdout, stderr = process.communicate()
except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e}")

print("Streaming finished.")
