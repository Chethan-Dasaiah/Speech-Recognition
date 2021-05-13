import speech_recognition as sr
from os import path


def recorded_audio_speech2Text(file):

    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)),"record\\"+ file)

    r = sr.Recognizer()

    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)

    try:
        textdata = r.recognize_google(audio)
        #textdata = r.recognize_sphinx(audio)
        print("Text data: " + textdata)
        return textdata

    except sr.UnknownValueError:
        print(" Audio Error")

    except sr.RequestError as e:
        print("Could not request results from Google API; {0}".format(e))


def live_audio_speech2Text():

    #prints number of microphones available
    '''for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Speak Anything :")
        audio = r.listen(source)

    try:
        textdata = r.recognize_google(audio)
        #textdata = r.recognize_sphinx(audio)

        print("You said : {}".format(textdata))
        return textdata

    except sr.UnknownValueError:
        print(" Audio Error")

    except sr.RequestError as e:
        print("Could not request results from Google API; {0}".format(e))

