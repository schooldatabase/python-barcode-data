
############# pip install pyaudio pydub ######################
########### speek recoding ###############
import pyaudio
import wave
from pydub import AudioSegment

def record_audio(output_filename, duration=5, sample_rate=44100, channels=2, chunk=1024):
    try:
        p = pyaudio.PyAudio()

        stream = p.open(format=pyaudio.paInt16,
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=chunk)

        print("Recording...")

        frames = []
        for i in range(0, int(sample_rate / chunk * duration)):
            data = stream.read(chunk)
            frames.append(data)

        print("Finished recording.")

        stream.stop_stream()
        stream.close()
        p.terminate()

        with wave.open(output_filename, 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
            wf.setframerate(sample_rate)
            wf.writeframes(b''.join(frames))
    
    except Exception as e:
        print(f"Error during recording: {e}")

if __name__ == "__main__":
    try:
        output_wav_file = "output.wav"
        output_mp3_file = "output.mp3"
        data = int(input("Enter duration number = "))
        record_audio(output_wav_file, duration=data)
    
    except Exception as e:
        print(f"Error in main execution: {e}")












#####################################################

# import pyaudio
# import wave
# from pydub import AudioSegment

# def record_audio(output_filename, duration=5, sample_rate=44100, channels=2, chunk=1024):
#     try:
#         p = pyaudio.PyAudio()

#         stream = p.open(format=pyaudio.paInt16,
#                         channels=channels,
#                         rate=sample_rate,
#                         input=True,
#                         frames_per_buffer=chunk)

#         print("Recording...")

#         frames = []
#         for i in range(0, int(sample_rate / chunk * duration)):
#             data = stream.read(chunk)
#             frames.append(data)

#         print("Finished recording.")

#         stream.stop_stream()
#         stream.close()
#         p.terminate()

#         with wave.open(output_filename, 'wb') as wf:
#             wf.setnchannels(channels)
#             wf.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
#             wf.setframerate(sample_rate)
#             wf.writeframes(b''.join(frames))
    
#     except Exception as e:
#         print(f"Error during recording: {e}")

# # def convert_wav_to_mp3(input_wav_file, output_mp3_file):
# #     try:
# #         sound = AudioSegment.from_wav(input_wav_file)
# #         sound.export(output_mp3_file, format="mp3")
    
# #     except Exception as e:
# #         print(f"Error during conversion: {e}")

# if __name__ == "__main__":
#     try:
#         output_wav_file = "output.wav"
#         output_mp3_file = "output.mp3"
#         data = int(input("Enter duration number = "))
#         record_audio(output_wav_file, duration=data)
#         # convert_wav_to_mp3(output_wav_file, output_mp3_file)
    
#     except Exception as e:
#         print(f"Error in main execution: {e}")
