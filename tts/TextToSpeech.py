import pyttsx3


def my_chat():
    text_speech = pyttsx3.init()

    while True:
        answer = input("Shubhabrata: ")

        text_speech.say(answer)
        text_speech.runAndWait()

        if answer == 'Bye':
            break


def my_file(book, audiofile):
    text_speech = pyttsx3.init()
    file = open(book, 'r')

    txt = file.read()
    text_speech.save_to_file(txt, audiofile)
    text_speech.runAndWait()
