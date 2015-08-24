# -*- coding: utf-8 -*-

import wget


def run():
    with open('src.txt', 'r') as f:
        lines = f.readlines()
        for l in lines:
            download(l)
            return
    print "all done!"


def download(url):
    print "downloading %s" % url
    filename = wget.download(url)
    print filename


if __name__ == "__main__":
    run()
