# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import sinar.article


class SinarArticleLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=sinar.article)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'sinar.article:default')


SINAR_ARTICLE_FIXTURE = SinarArticleLayer()


SINAR_ARTICLE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SINAR_ARTICLE_FIXTURE,),
    name='SinarArticleLayer:IntegrationTesting',
)


SINAR_ARTICLE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SINAR_ARTICLE_FIXTURE,),
    name='SinarArticleLayer:FunctionalTesting',
)


SINAR_ARTICLE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SINAR_ARTICLE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='SinarArticleLayer:AcceptanceTesting',
)
