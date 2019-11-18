import speech_recognition as sr
import webbrowser as wb

def searchItem(obj,url):
    obj = sr.Recognizer()
#    url = 'https://data-flair.training/blogs/{}-tutorials-home/'
    with sr.Microphone() as source:
        obj.adjust_for_ambient_noise(source, duration=5)
        print("\nSearch the items :")
        print('\n[ SPEAK ] : ',end=' ')
        audio = obj.listen(source, timeout=5)

        try:
            get = obj.recognize_google(audio)
            print(get)
            wb.get().open_new(url.format(get))
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError:
            print('failed')
 
r1 = r2 = r3 = sr.Recognizer()
#r2 = sr.Recognizer()
#r3 = sr.Recognizer()

with sr.Microphone() as source:
    print('PLease wait. Calibrating microphone....')
    r3.adjust_for_ambient_noise(source, duration=5)
    print("\n\nAction :\n -> Text\n-> Videos")
    print("\n[ SPEAK ] : ",end=' ')
    audio = r3.listen(source, timeout=5)
    print("{}".format(r3.recognize_google(audio)))

    if "text" in r2.recognize_google(audio):
        url = 'https://data-flair.training/blogs/{}-tutorials-home/'
        searchItem(r2,url)
    elif 'videos' in r1.recognize_google(audio):
        url = 'https://www.youtube.com/results?search_query={}'
        searchItem(r1,url)
    else:
        print("\nSorry , try again next time.")
print("\n\t[ Done ]")
