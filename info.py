# -*- coding: utf-8 -*-

import util


def run():
    posts = util.get_all_posts()
    [print_line(l) for l in posts]


def print_line(l):
    (PostID, URL, AddTime, State) = l
    state = 'unknown'
    if State == 0:
        state = 'new'
    elif State == 1:
        state = 'fetched'
    print '%d %s %s' % (PostID, URL, state)


if __name__ == "__main__":
    run()
