# -*- coding: utf-8 -*-

import sys
import re
import urlparse
import os
import util


def run(blogname):
    homeurl = "http://{0}.tumblr.com".format(blogname)
    archiveurl = "{0}/archive".format(homeurl)
    fetch(archiveurl)
    print 'all done!'


def fetch(url):
    print "fetching %s" % url
    with open('fetching.txt', 'w') as f:
        f.write(url)

    page = util.download(url)

    posts = find_all_posts(page)

    with open('posts.txt', 'a') as f:
        [f.write(p + '\n') for p in posts]
        print "%d posts fetched" % len(posts)

    next_page_link = find_next_page_url(page)

    if next_page_link is not None:
        return fetch(urlparse.urljoin(url, next_page_link))
    else:
        os.unlink("fetching.txt")
        return


def find_all_posts(content):
    postRegex = re.compile("http://[^.]+.tumblr.com/post/\d+[^\"]", re.IGNORECASE | re.MULTILINE)
    matches = postRegex.findall(content)
    return matches


def find_next_page_url(content):
    nextPageRegex = re.compile("(/archive\?before_time=\d+)",
                               re.IGNORECASE | re.MULTILINE)
    nextPageMatch = nextPageRegex.search(content)
    if nextPageMatch != None:
        return nextPageMatch.group(1)
    return None


if __name__ == "__main__":
    if len(sys.argv) == 2:
        run(sys.argv[1])
    else:
        print "invalid request, sample: python spider.py massimo"