#libery
import speech_recognition as sr


def takeCommand():
    #take voice input and string output
    r = sr.Recognizer()

    with sr.Microphone(0) as source: # Setup your mic number hare------------------------------------------------------ Mick
        print('I am listening you...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio,language='en-in') # Change Language from hare ---------------------------------------- Language
        print(f'Your Command:{query}\n')

    except Exception as e:
        
        print('Say that agin please...')
        return 'None'
    return query




"""while True:
    query = takeCommand().lower()
    print('Your Text is :', query)"""