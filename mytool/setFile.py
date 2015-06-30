# -*- coding: UTF-8 -*-

import glob

class SetFile(object):
    @staticmethod
    def set_file():
        file_list = glob.glob('*')
        print 'Wybierz numer pliku: '
        for i, f in enumerate(file_list):
            if not f.endswith('py'):
                print i+1, f
        file_index = raw_input('Podaj numer pliku: ')
        try:
            file_index = int(file_index)-1
            print 'Wybran plik: ', file_list[file_index]
            return file_list[file_index]
        except:
            print 'Cos poszlo nie tak'
            return False





class inna(SetFile):
    def __init__(self, cos):
        print cos
        set_file()
class jeszczeinna(object):
    def __init__(self):
        X = SetFile.set_file()

if __name__ == '__main__':
    X= jeszczeinna()