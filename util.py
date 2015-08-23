# -*- coding: utf-8 -*-

import urllib2
import urlparse


def download(url):
    o = urlparse.urlparse(url)
    hdr = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Host': o.netloc,
        'Path': o.path.strip(),
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.45 Safari/537.36'
    }
    req = urllib2.Request(url, headers=hdr)
    page = urllib2.urlopen(req)
    return page.read()
