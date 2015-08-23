# -*- coding: utf-8 -*-

import util
import re


def run():
    with open('posts.txt', 'r') as f:
        lines = f.readlines()
        for l in lines:
            fetch(l.strip())
            return
    print "all done!"


def fetch(url):
    print "fetching %s" % url
    page = get_real_page_data(url)


def get_real_page_data(url):
    data = util.download(url)
    src = get_iframe_url(data)
    if src is not None:
        print "iframe found, look into: %s" % src
        return get_real_page_data(src)
    return data


def get_iframe_url(data):
    srcReg = re.compile('<iframe src=[\'"]([^\'"]+)[\'"]', re.IGNORECASE | re.MULTILINE)
    m = srcReg.search(data)
    if m is not None:
        return m.group(1)
    return None

if __name__ == "__main__":
    run()
