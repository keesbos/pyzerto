# -*- coding: utf-8 -*-
'''Zerto alert object'''

from zertoobject import ZertoObject
from misc import parse_timestamp


class Alert(ZertoObject):

    def __init__(self, **kwargs):
        self.values = kwargs
        self.vpgs = list([
            i['identifier'] for i in kwargs.get('AffectedVpgs', [])
        ])
        self.zorgs = list([
            i['identifier'] for i in kwargs.get('AffectedZorgs', [])
        ])
        self.help_identifier = kwargs.get('HelpIdentifier')
        self.site_identifier = (kwargs.get('Site') or {}).get('identifier')
        self.turned_on = parse_timestamp(kwargs['TurnedOn'])
        self.description = kwargs['Description']
        self.entity = kwargs.get('Entity')
        self.level = kwargs.get('Level')
        self.is_dismissed = kwargs.get('IsDismissed')

    def __str__(self):
        return 'identifier={0}, occurred_on={1}, event_type={2}'.format(
            self.identifier, self.occurred_on, self.event_type)


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
