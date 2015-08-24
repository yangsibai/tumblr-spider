# -*- coding: utf-8 -*-

import sys
import re
import urlparse
import util


def run(blogname):
    homeurl = "http://{0}.tumblr.com".format(blogname)
    archiveurl = "{0}/archive".format(homeurl)
    fetch(archiveurl)
    print 'all done!'


def fetch(url):
    print "fetching %s" % url
    page = util.download(url)
    posts = find_all_posts(page)
    if len(posts) > 0:
        [util.insert_post(p) for p in posts]
        print "%d posts fetched" % len(posts)
        next_page_link = find_next_page_url(page)
        if next_page_link is not None:
            return fetch(urlparse.urljoin(url, next_page_link))
        else:
            return
    else:
        return


def find_all_posts(content):
    pattern = re.compile("http://[^.]+.tumblr.com/post/\d+[^\"]", re.IGNORECASE | re.MULTILINE)
    matches = pattern.findall(content)
    return matches


def find_next_page_url(content):
    pattern = re.compile("(/archive\?before_time=\d+)",
                               re.IGNORECASE | re.MULTILINE)
    match = pattern.search(content)
    if match is not None:
        return match.group(1)
    return None


if __name__ == "__main__":
    if len(sys.argv) == 2:
        util.create_table()
        run(sys.argv[1])
    else:
        print "invalid request, sample: python spider.py massimo"