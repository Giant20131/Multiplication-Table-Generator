import pyttsx3
import time

text_speech = pyttsx3.init()
num = int(input("Enter a number to generate its multiplication table: "))

for i in range(1,11):
    print(num,"X",i,"=",i*num)
    ans= num,i,"are",i*num
    text_speech.say(ans)
    time.sleep(5.5)
    text_speech.runAndWait()