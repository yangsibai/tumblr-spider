# -*- coding: utf-8 -*-

import util


def run():
    with open('src.txt', 'r') as f:
        lines = f.readlines()
        for l in lines:
            download(l)
            return
    print "all done!"


def download(url):
    print "downloading %s" % url
    d = util.download(url)
    with open('test.mp4', 'w') as f:
        f.write(d)


if __name__ == "__main__":
    run()
