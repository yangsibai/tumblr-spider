# -*- coding: utf-8 -*-

import util
import re


def run():
    with open('posts.txt', 'r') as f:
        lines = f.readlines()
        with open('iframes.txt', 'w') as fr:
            for l in lines:
                print "fetching %s" % l
                src = get_iframe_url(l)
                if src is not None:
                    fr.write(src + "\n")
                return


def get_iframe_url(url):
    print 'fetching %s' % url
    page = util.download(url)
    srcReg = re.compile('<iframe src="([^"]+)"', re.IGNORECASE | re.MULTILINE)
    m = srcReg.search(page)
    if m is not None:
        return m.group(1)
    return None

if __name__ == "__main__":
    run()
