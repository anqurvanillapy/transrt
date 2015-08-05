#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

TRANSLATE_HELP = '''
Commmands     Functions
---------     --------------------------
    'f'       Forwarding
    'b'       Backwarding
    's'       Shutting Down,
              or Skipping Search Results
---------     --------------------------'''

def parse_argument():

    parser = argparse.ArgumentParser(
        description='A simple manual translator of SubRip file'
        )

    parser.add_argument(
        'filename',
        metavar='filename',
        action='store',
        help='input file name'
        )

    parser.add_argument(
        '-o', '--output',
        dest='ofile',
        metavar='filename',
        action='store',
        default='a.srt',
        help='output file name'
        )

    search_parser = parser.add_mutually_exclusive_group()

    search_parser.add_argument(
        '-kn', '--keynumber',
        dest='kn',
        metavar='keynumber',
        type=int,
        action='store',
        help='the key number to search for'
        )

    search_parser.add_argument(
        '-kwd', '--keyword',
        dest='kwd',
        metavar='keyword',
        action='store',
        help='the keyword to search for'
        )

    return parser.parse_args()

class Transrt(object):

    def __init__(self, args):

        self.filename = args.filename
        self.ofile = args.ofile
        self.kn = args.kn
        self.kwd = args.kwd

        self.not_found = False

        self.initFile(self.filename)

    def initFile(self, filename):

        try:
            self.srt = open(filename, 'r')
            self.pack(self.srt)
        except IOError:
            print "Unable to open file '%s'" % filename

    def pack(self, srt):

        print 'Packing file...'

        srt = filter(None, srt.read().split('\n'))
        self.packed = []
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

                self.packed.append(srt_dict)
                num += 1
            else:
                index += 1

        # print self.packed
        if self.packed:
            print 'Success'
            print TRANSLATE_HELP

            if self.kn:
                self.searchKeynum(self.kn)
            elif self.kwd:
                self.searchKeywd(self.kwd)
            else:
                self.translate()
        else:
            print 'Unable to pack the file'

    def translate(self, count=0, skip=False):

        srt = self.packed
        ofile = open(self.ofile, 'w')
        stdio = []
        ioitem = None
        self.shut = self.back = self.restart = False

        if skip:
            temp = 0
            while temp < count:
                ioitem = str(srt[temp]['num']) + '\n' + srt[temp]['dura'] + '\n'
                for item in srt[temp]['script']:
                    ioitem += item + '\n'
                for item in srt[temp]['cont']:
                    ioitem += item + '\n'
                ioitem += '\n'
                stdio.append(ioitem)
                temp += 1

        while count < len(srt):
            print '\n' + str(srt[count]['num'])
            print srt[count]['dura']
            for item in srt[count]['cont']:
                print item
            if count == len(srt) - 1:
                print '(This is the last line.)'
            else:
                preview = count + 1
                print '\n(Next line is'
                for item in srt[preview]['cont']:
                    print '\t' + item
                print ')'

            while True:
                item = raw_input('>>> ')
                # 'f' for Forwarding
                if item == 'f':
                    break
                # 's' for Shutting Down
                elif item == 's':
                    self.shut = True
                    break
                # 'b' for Backwarding
                elif item == 'b':
                    self.back = True
                    break
                # 'r' for Restarting
                elif item == 'r':
                    self.restart = True
                    break
                srt[count]['script'].append(item)
                srt[count]['script'] = filter(None, srt[count]['script'])

            if self.back:
                if len(stdio):
                    to_del = len(stdio) - 1
                    del stdio[to_del]
                    count -= 1
                srt[count]['script'] = []
                self.back = False
                continue

            if self.restart:
                srt[count]['script'] = []
                self.restart = False
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

        ofile.close()

    def searchKeynum(self, kn):

        for item in self.packed:
            if kn == item['num']:
                print "\nKey number '%d' Found" % kn
                self.not_found = False
                self.translate(kn-1, True)
                break
            else:
                self.not_found = True

        if self.not_found:
            print "Key number '%d' Not Found" % kn

    def searchKeywd(self, kwd):

        count = 0
        temp = 1

        for pack in self.packed:
            for item in pack['cont']:
                if kwd in item:
                    count += 1

        if count:
            print "Got %d Results" % count

        for pack in self.packed:
            for item in pack['cont']:
                if kwd in item:
                    print "\nKeyword '%s' Found in '%d'" % (kwd, pack['num'])
                    print "Now on %d / %d, %d Left" % (temp, count, count - temp)
                    self.not_found = False
                    temp += 1
                    self.translate(pack['num']-1, True)
                else:
                    self.not_found = True

        if self.not_found:
            print "Keyword '%s' Not Found" % kwd

def main():

    args = parse_argument()
    transrt = Transrt(args)


if __name__ == '__main__':
    main()