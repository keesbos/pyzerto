# -*- coding: utf-8 -*-
'''Zerto VirtualizationSite object'''

from zertoobject import ZertoObject


class VirtualizationSite(ZertoObject):

    def __init__(self, **kwargs):
        self.values = kwargs
        self.name = kwargs['VirtualizationSiteName']
        self.identifier = kwargs['SiteIdentifier']

    def __str__(self):
        return 'name={0}, identifier={1}'.format(
            self.name, self.identifier)


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
