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
            print "Unable to open file %s" % filename

    def pack(self, srt):

        srt = filter(None, srt.read().split('\n'))

        print srt

    def searchKeynum(self, kn):

        print kn

    def searchKeywd(self, kwd):

        print kwd

if __name__ == '__main__':

    args = parse_argument()
    transrt = Transrt(args)