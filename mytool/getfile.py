# -*- coding: UTF-8 -*-

import glob


def set_file():
    file_list = glob.glob('*')
    print 'Wybierz numer pliku: '
    for i, f in enumerate(file_list):
        if not f.endswith('py*'):
            print i+1, f
    file_index = raw_input('Podaj numer pliku: ')
    try:
        file_index = int(file_index)-1
        print 'Wybran plik: ', file_list[file_index]
        return file_list[file_index]
    except:
        print 'Cos poszlo nie tak'
        return False

if __name__ == '__main__':
    main()