# -*- coding: utf-8 -*-


def find_duplicate():
    with open('posts.txt', 'r') as f:
        lines = f.readlines()
        s = set()
        for l in lines:
            if l in s:
                print "%s exist"

if __name__ == "__main__":
    find_duplicate()
