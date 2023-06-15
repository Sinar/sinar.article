# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.app.dexterity import textindexer
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.app.z3cform.widget import SelectFieldWidget
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
# from zope import schema
from zope.interface import implementer
from sinar.article import _


class IArticle(model.Schema):
    """ Marker interface and Dexterity Python Schema for Article
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('article.xml')

    textindexer.searchable('article_body')
    article_body = RichText(
        title=_(u'Article Body'),
        description=_(u'Main article body text'),
        required=False
    )


@implementer(IArticle)
class Article(Container):
    """ Content-type class for IArticle
    """
