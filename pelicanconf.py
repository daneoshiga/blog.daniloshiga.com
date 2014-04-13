#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Danilo Shiga'
SITENAME = u'Danilo Shiga'
SITEURL = 'http://localhost:8000'
DISQUS_SITENAME = "blog-daniloshiga"

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
AUTHOR_URL = 'author/'
AUTHOR_SAVE_AS = 'author/{slug}.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

PATH = 'content'

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

STATIC_PATHS = [
    'extra/favicon.ico',
    'extra/.htaccess',
]
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/.htaccess': {'path': '.htaccess'},
}

#from pelican.plugins import related_posts
PLUGIN_PATH = '../pelican-plugins'
PLUGINS = ['googleplus_comments', ]

ASSET_SOURCE_PATHS = (
    'static/css',
)

THEME = 'themes/toasted'

DISPLAY_CATEGORIES_ON_MENU = False

MD_EXTENSIONS = ['codehilite(linenums=True)', 'extra', 'fenced_code']

# variables used inside theme
# GITHUB_URL = 'https://github.com/daneoshiga/blog.daniloshiga.com'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
