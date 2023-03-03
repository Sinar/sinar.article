# -*- coding: utf-8 -*-

# from sinar.article import _
from Products.Five.browser import BrowserView
from zope.interface import Interface

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IArticleView(Interface):
    """ Marker Interface for IArticleView"""


class ArticleView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('article_view.pt')

    def __call__(self):
        # Implement your own actions:
        return self.index()

    def code(self):
        value = 1 + 1
        return value

