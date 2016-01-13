#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from collections import OrderedDict


AUTHOR = 'Dunderlabs'
SITENAME = '__labs__'
SITEURL = ''
TITLE_SITE = 'DunderLabs - Respirando inovação, expirando qualidade'

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
    4 amigos com gostos igualmente parecidos e diferentes, reunindo
    conhecimento, experiências e muitas dúvidas sobre: Front-End,
    Python/Django, Linux, JS e etc. Devolvemos à comunidade o que em muitos
    momentos ela nos ofereceu.
'''

META_KEYWORDS = [
    'pug-pi', 'python', 'parnaiba', 'desenvolvimento', 'web', 'django'
]

SITE_LOGO = '/images/logo1.jpg'

OPEN_GRAPH_IMAGE = "/images/logo1.jpg"

TWITTER = '@dunderlabs'

MEMBROS = OrderedDict((
    ('Patrick Mazulo', {
        'email': 'pmazulo@gmail.com',
        'twitter': '@ericleribertson',
        'github': 'mazulo'
    }),
))
