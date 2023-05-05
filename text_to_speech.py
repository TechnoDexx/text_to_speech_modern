"""
Демонстрация того, как можно читать текст из файла на разных языках.
Метод жутко примитивный - он создавался для того, чтобы изучить основы преобразования текста в речь.
Файл text.txt - список из предложений на разных языках (по одному на строку).
Метод признан примитивным из-за того, что слова на разных языках могут идти вперемешку.
Данный вариант можно использовать для озвучивания действий программ на разных языках.
"""

import gtts
import gtts.lang

from utils.speak_text import speak_from_file

# import utils.speak_text as s_t
langs_has_run = False


class GetLangs:
    """
    Класс, получающий список языков, поддерживаемых библиотекой GTTS
    """
    def __init__(self):
        self.has_run = False

    def show_langs(self):
        if self.has_run:
            return
        else:
            langs = gtts.lang.tts_langs()
            for key in langs:
                print('\'{0}\' {1}'.format(key, langs[key]))


if __name__ == '__main__':
    # get_words('text.txt', 'r')
    speak_from_file('text.txt', 'r')
