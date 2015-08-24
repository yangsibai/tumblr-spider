# -*- coding: utf-8 -*-

import wget
import util
import sys


def run():
    sources = util.get_all_new_sources()
    i = 0
    for src in sources:
        i += 1
        (SourceID, PostID, URL, Type, State) = src
        print '%d %s' % (i, URL)
        download(URL)
        util.set_source_downloaded(SourceID)

    print "all done!"


def download(url):
    print "downloading %s" % url
    try:
        wget.download(url)
    except:
        print 'error occurred at %s : %s' % (url, sys.exc_info()[0])


if __name__ == "__main__":
    run()
