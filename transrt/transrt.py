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
        action='store',
        default='a.srt'
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
        self.ofile = args.ofile
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
        packed = []
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

                packed.append(srt_dict)
                num += 1
            else:
                index += 1

        # print packed
        if packed:
            print 'Success'
            self.translate(packed)
        else:
            print 'Unable to pack the file'

    def translate(self, srt):

        ofile = open(self.ofile, 'w')
        count = 0
        stdio = []
        ioitem = None
        self.shut = False
        self.back = False

        while count < len(srt):
            print srt[count]['num']
            print srt[count]['dura']
            for item in srt[count]['cont']:
                print item

            while True:
                item = raw_input('>> ')
                # 'f' for Forwarding
                if item == 'f':
                    break
                # 's' for Shutting Down
                elif item == 's':
                    self.shut = True
                    break
                # 'b' for Backwarding
                elif item == 'b' and len(stdio) != 0:
                    self.back = True
                    break
                srt[count]['script'].append(item)
                srt[count]['script'] = filter(None, srt[count]['script'])

            if self.back:
                del stdio[len(stdio)-1]
                count -= 1
                srt[count]['script'] = []
                self.back = False
                continue

            ioitem = str(srt[count]['num']) + '\n' + srt[count]['dura'] + '\n'
            for item in srt[count]['script']:
                ioitem += item + '\n'
            for item in srt[count]['cont']:
                ioitem += item + '\n'
            ioitem += '\n'
            stdio.append(ioitem)
            count += 1

            if self.shut:
                break

        for item in stdio:
            ofile.write(item)

    def searchKeynum(self, kn):

        print kn

    def searchKeywd(self, kwd):

        print kwd

if __name__ == '__main__':

    args = parse_argument()
    transrt = Transrt(args)