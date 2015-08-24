# -*- coding: utf-8 -*-

import urllib2
import urlparse
import sqlite3
import time


POST_STATE_NEW = 0
POST_STATE_FETCHED = 1


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


def get_conn():
    """
        get db connection
    """
    return sqlite3.connect('tumblr.db')


def create_table():
    conn = get_conn()
    c = conn.cursor()

    # create table posts
    c.execute('''CREATE TABLE IF NOT EXISTS Post(
        PostID INTEGER PRIMARY KEY AUTOINCREMENT,
        URL TEXT, AddTime INTEGER, State INTEGER)''')

    # create table sources
    c.execute('''CREATE TABLE IF NOT EXISTS Source(
        SourceID INTEGER PRIMARY KEY AUTOINCREMENT,
        PostID INTEGER, URL TEXT, Type TEXT)''')

    conn.commit()
    conn.close()


def insert_post(url):
    conn = get_conn()
    c = conn.cursor()

    c.execute('SELECT * FROM Post WHERE URL = ?', (url, ))
    if c.fetchone():
        print '%s exists' % url
        conn.close()
        return

    c.execute('''INSERT INTO Post(URL, AddTime, State)
        VALUES(?, ?, ?)''', (url, time.time(), POST_STATE_NEW))

    conn.commit()
    conn.close()
    return c.lastrowid


def insert_source(postid, sourceurl, type='video'):
    conn = get_conn()
    c = conn.cursor()

    c.execute('SELECT * FROM Source WHERE URL = ?', (sourceurl, ))
    if c.fetchone():
        print '%s exists' % sourceurl
        conn.close()
        return

    c.execute('''INSERT INTO Source(PostID, URL, Type)
        VALUES(?, ?, ?)''', (postid, sourceurl, type))

    conn.commit()
    conn.close()
    return c.lastrowid


def set_post_fetched(postid):
    conn = get_conn()
    c = conn.cursor()

    c.execute('''UPDATE Post
        SET State = ?
        WHERE PostID = ?''', (POST_STATE_FETCHED, postid))

    conn.commit()
    conn.close()


def get_all_new_posts():
    conn = get_conn()
    c = conn.cursor()
    c.execute('''SELECT * FROM Post WHERE State = ?''', (POST_STATE_NEW, ))
    posts = c.fetchall()
    conn.close()
    return posts


def get_all_posts():
    conn = get_conn()
    c = conn.cursor()
    c.execute('''SELECT * FROM Post''')
    posts = c.fetchall()
    conn.close()
    return posts


def get_all_sources():
    conn = get_conn()
    c = conn.cursor()
    c.execute('SELECT * FROM Source')
    sources = c.fetchall()
    conn.close()
    return sources
