#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sandeep Jadoonanan'
SITENAME = u'Smallcode Blog'
ALT_NAME = u"> .logs"
SITEURL = 'http://blog.smallcode.me'
SITESUBTITLE = u"The web is awesome."
DESCRIPTION = u"Programming snippets, Python code, Random thoughts."
FAVICON = 'favicon.ico'
FAVICON_TYPE = 'image/vnd.microsoft.icon'

META_IMAGE = SITEURL + "/img/og_logo.png"
META_IMAGE_TYPE = "image/png"

PATH = 'content'
STATIC_PATHS = ["img", "pdf", "pages", "feeds", "extra"]
EXTRA_PATH_METADATA = {
  'extra/robots.txt': {'path': 'robots.txt'},
  'extra/favicon.ico': {'path': 'favicon.ico'}
}

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

THEME = "themes/mg"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Django', 'https://www.djangoproject.com/'),
         ('Python.org', 'http://python.org/'),
         ('Ambient Music', 'https://www.youtube.com/user/cryochamberlabel'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/sandcoder'),
		    ('google-plus-square', 'https://plus.google.com/+SmallcodeMe'),
		    ('github', 'https://github.com/tunedmystic'),
		    ("linkedin-square", "https://linkedin.com/in/sandeepjadoonanan"),
		    ('info-circle', 'http://smallcode.me'),)


DEFAULT_PAGINATION = 5

# Set to True if you want document-relative URLs when developing
RELATIVE_URLS = False

FOOTER = ("&copy; Sandeep Jadoonanan.<br>" +
           "<em style=\"color: #999;\">Technology is as dangerous as it is beautiful.</em>")
              
# mg specific settings.
SHARE = True
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
DIRECT_TEMPLATES = ('index', 'categories', 'archives', 'search', 'tipue_search')
TIPUE_SEARCH_SAVE_AS = 'tipue_search.json'
TWITTER_USERNAME = "sandcoder"
#DISQUS_SITENAME = "smallcodeblog"

