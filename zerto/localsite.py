# -*- coding: utf-8 -*-
'''Zerto LocalSite object'''

from zertoobject import ZertoObject


class LocalSite(ZertoObject):

    def __init__(self, **kwargs):
        self.values = kwargs
        self.name = kwargs['SiteName']
        self.identifier = kwargs['SiteIdentifier']
        self.version = kwargs.get('Version')
        self.location = kwargs.get('Location')
        self.utc_offset = kwargs.get('UtcOffsetInMinutes')
        self.is_replication_to_self_enabled = kwargs.get(
            'IsReplicationToSelfEnabled')
        self.contact_name = kwargs.get('ContactName')
        self.contact_email = kwargs.get('ContactEmail')
        self.contact_phone = kwargs.get('ContactPhone')

    def __str__(self):
        return 'name={0}, identifier={1}, version={2}'.format(
            self.name, self.identifier, self.version)


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
