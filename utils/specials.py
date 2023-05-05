"""
Следующие две функции необходимы для того, чтобы подавить вывод на экран приглашения библиотеки PyGame
присоединиться к её сообществу.
"""
import sys
import os


def disablePrint():
    """
    Функция подавляет вывод на экран
    :return: None
    :rtype: None
    """
    sys.stdout = open(os.devnull, 'w')


def enablePrint():
    """
    Функция восстанавливает вывод на экран
    :return: None
    :rtype: None
    """
    sys.stdout = sys.__stdout__
