# -*- coding: utf-8 -*-

import util
import re


def run():
    with open('posts.txt', 'r') as f:
        lines = f.readlines()
        if len(lines) > 0:
            with open("src.txt", 'a') as sf:
                for l in lines:
                    url = l.strip()
                    src = fetch(url)
                    if src is not None:
                        print "source %s find at %s" % (src, url)
                        sf.write(src + '\n')
                    else:
                        print "no source at %s" % url
                    return
    print "all done!"


def fetch(url):
    print "fetching %s" % url
    page = get_real_page_data(url)
    src = get_source_url(page)
    return src


def get_real_page_data(url):
    print "see if page contain real data: %s " % url
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


def get_source_url(data):
    srcReg = re.compile('<source src=[\'"]([^\'"]+)[\'"]', re.IGNORECASE |
                        re.MULTILINE)
    m = srcReg.search(data)
    if m is not None:
        return m.group(1)
    return None

if __name__ == "__main__":
    run()
