import speech_recognition as sr
def takecommand():
    r = sr.Recognizer()    
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1 
        #waits for one second before a sentence is considered complete
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-Pk")
        print(f"User said: {query}")
    except Exception as e:
        print("Please speak again")
        query = ''
    return query


takecommand()