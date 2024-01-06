import cv2

cap = cv2.VideoCapture(0)  # Use camera index 0 for the default camera

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(r'1 vinod video data\output_video1.mp4', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()

    # Process the frame as needed

    # Display the frame
    cv2.imshow('Frame', frame)

    # Write the frame to the output video file
    out.write(frame)

    key = cv2.waitKey(1)  # Reduce waitKey time to 1ms for smoother key handling

    if key == ord('q'):
        break

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()



















# import cv2
# import numpy as np
# import pyaudio
# import wave

# # Video settings
# cap = cv2.VideoCapture(0)  # Use camera index 0 for the default camera

# # Audio settings
# FORMAT = pyaudio.paInt16
# CHANNELS = 1
# RATE = 44100
# CHUNK = 1024

# p = pyaudio.PyAudio()
# stream = p.open(format=FORMAT,
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 frames_per_buffer=CHUNK)

# # Define the codec and create a VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter('1 vinod video data\output_video.mp4', fourcc, 20.0, (640, 480))

# while cap.isOpened():
#     ret, frame = cap.read()

#     # Process the video frame as needed

#     # Display the video frame
#     cv2.imshow('Frame', frame)

#     # Read audio data from the microphone
#     audio_data = stream.read(CHUNK)
#     audio_array = np.frombuffer(audio_data, dtype=np.int16)

#     # Process the audio data as needed

#     # Write the video frame and audio data to the output video file
#     out.write(frame)

#     key = cv2.waitKey(1)  # Reduce waitKey time to 1ms for smoother key handling

#     if key == ord('q'):
#         break

# # Release everything when done
# cap.release()
# out.release()
# cv2.destroyAllWindows()

# # Stop audio stream and close PyAudio
# stream.stop_stream()
# stream.close()
# p.terminate()




































# import cv2

# cap = cv2.VideoCapture(0)  # Use camera index 0 for the default camera

# # Define the codec and create a VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter('1 vinod video data\output_video1.mp4', fourcc, 20.0, (640, 480))

# while cap.isOpened():
#     ret, frame = cap.read()

#     # Process the frame as needed

#     # Display the frame
#     cv2.imshow('Frame', frame)

#     # Write the frame to the output video file
#     out.write(frame)

#     key = cv2.waitKey(1)  # Reduce waitKey time to 1ms for smoother key handling

#     if key == ord('q'):
#         break

# # Release everything when done
# cap.release()
# out.release()
# cv2.destroyAllWindows()









# import cv2

# cap = cv2.VideoCapture(0)  # Use camera index 0 for the default camera

# while cap.isOpened():
#     ret, frame = cap.read()

#     # Process the frame as needed

#     cv2.imshow('Frame', frame)

#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
















"""# import cv2

# cap = cv2.VideoCapture(0)  # Use camera index 0 for the default camera

# while cap.isOpened():
#     ret, frame = cap.read()

#     # Process the frame as needed

#     cv2.imshow('Frame', frame)

#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()



"""





























