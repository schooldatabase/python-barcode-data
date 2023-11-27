####################### pip install SpeechRecognition ##################
####### python any library used speek audio file to text format write code  ##############


import speech_recognition as sr

def audio_to_text(audio_file):
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
    audio_file = "output.wav"  # Replace with the path to your audio file
    text_result = audio_to_text(audio_file)
