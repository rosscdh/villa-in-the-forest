#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Ross Crawford'dHeureuse"
SITENAME = u'The Villa in the forest'
SITEURL = 'http://localhost:8000'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'en'
ARTICLE_LANG_URL = '{lang}/{slug}.html'
ARTICLE_LANG_SAVE_AS = '{lang}/{slug}.html'

# Blogroll
MENUITEMS =  (
	('Home', '/'),
)

# Social widget
SOCIAL = ()

# Extra pages
DISPLAY_PAGES_ON_MENU = True

STATIC_PATHS = ['images', 'js',]

DEFAULT_PAGINATION = 10

TYPOGRIFY = True

#THEME = 'pelican-themes/iris'
THEME = 'theme/iris'
