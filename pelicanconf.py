#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dunderlabs'
SITENAME = '__labs__'
SITEURL = ''

DISPLAY_PAGES_ON_MENU = True

PATH = 'content'

TIMEZONE = 'America/Fortaleza'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/dunderlabs'),
    ('github', 'https://github.com/dunderlabs'),
)

DEFAULT_PAGINATION = 10

MENUITEMS = (
    ('Pythonista Intermediário', 'pages/pythonista-intermediario'),
)

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/CNAME']

EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }

THEME = 'theme'

PLUGIN_PATHS = [
    'pelican-plugins'
]

PLUGINS = [
    'gravatar'
]


# Theme configs

COVER_IMG_URL = 'images/wallpaper.jpg'
TAGLINE = ''
DISQUS_SITENAME = 'dunderlabs'


# Custom configs
META_DESCRIPTION = '''
    O Grupy-DF é uma comunidade de usuários (profissionais e
    amadores) da linguagem Python, onde prezamos pela troca de
    conhecimento, respeito mútuo e diversidade (tanto de opinião
    quanto de tecnologias).
'''

META_KEYWORDS = [
    'pug-pi', 'python', 'parnaiba', 'desenvolvimento', 'web', 'django'
]
SITE_LOGO = '/images/logo1.png'
OPEN_GRAPH_IMAGE = "/images/logo1.png"
