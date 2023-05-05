import io

from gtts import gTTS

from utils.specials import enablePrint, disablePrint
from langdetect import detect

disablePrint()
import pygame

enablePrint()


def speak_from_file(file, mode='r'):
    """
    Функция читает файл построчно, определяет язык текста и зачитывает его
    :param file: имя файла
    :type file: string
    :param mode: режим открытия файла ('r' - чтение, по умолчанию)
    :type mode: string
    :return: None
    :rtype: None
    """
    print('Speaking...')
    with open(file, mode) as f:
        while True:

            txt = f.readline()
            if not txt:
                break
            # Определение пропускаемой строки (используется # в начале)
            if txt.startswith('#'):
                continue
            else:
                # Определение языка загруженной строки
                detect_lang = detect(txt)
                print('{0}'.format(detect_lang))

                try:
                    speak(txt, lang=detect_lang)
                except ValueError as err:
                    print(err)
                    continue

    print('Done.')


def speak(my_text, lang='en'):
    """
    Функция зачитывает текст, не сохраняя его на диск.
    :param my_text: Текст для озвучивания
    :type my_text: string
    :param lang: язык текста, на котором GTTS озвучит текст (английский по умолчанию)
    :type lang: string
    :return: None
    :rtype: None
    """
    with io.BytesIO() as f:
        gTTS(text=my_text, lang=lang).write_to_fp(f)
        f.seek(0)
        pygame.mixer.init()
        pygame.mixer.music.load(f)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
