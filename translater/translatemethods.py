from translate import Translator
import fileHandle.BookLiner


def translate_line(line, language):
    translator = Translator(to_lang=language)
    result = translator.translate(line)
    print(result)
    return result


def translate_chat():
    while True:
        answer = input("Shubhabrata: ")
        translator = Translator(to_lang='bn')
        result = translator.translate(answer)
        print(result)

        if answer == 'Thanks':
            break


def translate_text_book(src_book, language, des_book):

    lst = fileHandle.BookLiner.book_to_list(src_book)
    file = open(des_book, 'w')

    for line in lst:
        translator = Translator(to_lang=language)
        result = translator.translate(line)
        print(result)
        file.write(result+". ")

    file.close()
