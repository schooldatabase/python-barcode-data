import moviepy.editor as mp
import speech_recognition as sr

def video_to_text(video_file):
    # Extract audio from the video
    video_clip = mp.VideoFileClip(video_file)
    audio_clip = video_clip.audio
    audio_file = "audio_from_video.wav"
    audio_clip.write_audiofile(audio_file, codec='pcm_s16le', ffmpeg_params=["-ac", "1"])

    # Convert the extracted audio to text
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)  # Record the entire audio file

        try:
            text = recognizer.recognize_google(audio_data)
            print("Text from audio: ", text)
            return text
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

if __name__ == "__main__":
    video_file = "https://www.youtube.com/shorts/Wa3BqWDPsAg"  # Replace with the path to your video file
    text_result = video_to_text(video_file)

    # video_file = "C:\Users\user\Downloads\Justin-Bieber-Baby-Whatsapp-Status-_-English-Song-Whatsapp-Status720P_HD.mp4"  # Replace with the path to your video file
    # text_result = video_to_text(video_file)
