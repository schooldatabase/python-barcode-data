import pyttsx3  
# initialize Text-to-speech engine  
engine = pyttsx3.init()  
# convert this text to speech  
data = int(input("Enter a number with speed say = "))
engine.setProperty('rate', data)  # Speed of speech
engine.setProperty('volume', 1)

text = str(input("enter the text = "))
# text = " Vinod  vinod saini looking"  
engine.say(text)


engine.runAndWait()  
# engine.startLoop(text)