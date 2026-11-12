# -*- coding: utf-8 -*-
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from sinar.article.content.article import IArticle  # NOQA E501
from sinar.article.testing import SINAR_ARTICLE_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class ArticleIntegrationTest(unittest.TestCase):

    layer = SINAR_ARTICLE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_article_schema(self):
        fti = queryUtility(IDexterityFTI, name='Article')
        schema = fti.lookupSchema()
        self.assertEqual(IArticle, schema)

    def test_ct_article_fti(self):
        fti = queryUtility(IDexterityFTI, name='Article')
        self.assertTrue(fti)

    def test_ct_article_factory(self):
        fti = queryUtility(IDexterityFTI, name='Article')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IArticle.providedBy(obj),
            u'IArticle not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_article_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Article',
            id='article',
        )

        self.assertTrue(
            IArticle.providedBy(obj),
            u'IArticle not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('article', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('article', parent.objectIds())

    def test_ct_article_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Article')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_article_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Article')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'article_id',
            title='Article container',
        )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
