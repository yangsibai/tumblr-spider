# -*- coding: utf-8 -*-

import util


def run():
    posts = util.get_all_posts()
    print 'all posts:'
    [print_posts(l) for l in posts]
    print '\n\n'

    sources = util.get_all_sources()
    print 'all sources:'
    [print_source(l) for l in sources]


def print_posts(l):
    (PostID, URL, AddTime, State) = l
    state = 'unknown'
    if State == 0:
        state = 'new'
    elif State == 1:
        state = 'fetched'
    print '%d %s %s' % (PostID, URL, state)


def print_source(l):
    print '%d %d %s %s' % l


if __name__ == "__main__":
    run()
