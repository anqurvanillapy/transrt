#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

def parse_argument():

    parser = argparse.ArgumentParser(
        description='Translator of SubRip file'
        )

    parser.add_argument(
        'filename',
        metavar='filename',
        action='store'
        )

    parser.add_argument(
        '-o', '--output',
        dest='ofile',
        action='store'
        )

    parser.add_argument(
        '-n', '--search-number',
        dest='kn',
        action='store'
        )

    parser.add_argument(
        '-wd', '--search-word',
        dest='kwd',
        action='store'
        )

    return parser.parse_args()

class Transrt(object):

    def __init__(self, args):

        self.filename = args.filename
        self.kn = args.kn
        self.kwd = args.kwd

        self.initFile(self.filename)

        if self.kn:
            self.searchKeynum(self.kn)

        if self.kwd:
            self.searchKeywd(self.kwd)

    def initFile(self, filename):

        try:
            self.srt = open(filename, 'r')
            self.pack(self.srt)
        except IOError:
            raise "Unable to open file '%s'" % filename

    def pack(self, srt):

        print 'Packing file...'

        srt = filter(None, srt.read().split('\n'))
        srt_pack = []
        index = 0
        num = 1

        while index < len(srt):
            if srt[index].isdigit() and int(srt[index]) == num:
                    srt_dict = {
                        'num': None,
                        'dura': None,
                        'script': [],
                        'cont': []
                    }

                    srt_dict['num'] = num
                    index += 1
                    srt_dict['dura'] = srt[index]
                    index += 1

                    try:
                        while not (srt[index].isdigit() and int(srt[index]) == num + 1):
                            srt_dict['cont'].append(srt[index])
                            index += 1
                    except:
                        pass

                    srt_pack.append(srt_dict)
                    num += 1

            else:
                index += 1

        print 'Success'

    def searchKeynum(self, kn):

        print kn

    def searchKeywd(self, kwd):

        print kwd

if __name__ == '__main__':

    args = parse_argument()
    transrt = Transrt(args)