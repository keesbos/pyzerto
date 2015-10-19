# -*- coding: utf-8 -*-
'''Zerto event object'''

from zertoobject import ZertoObject
from misc import parse_timestamp
from constants import event_type, entity_type


class Event(ZertoObject):

    def __init__(self, **kwargs):
        self.values = kwargs
        self.identifier = kwargs['EventIdentifier']
        self.occurred_on = parse_timestamp(kwargs['OccurredOn'])
        self.description = kwargs['Description']
        self.site_name = kwargs.get('SiteName')
        self.completed_successfully = kwargs.get('EventCompletedSuccessfully')
        self.event_type = event_type[kwargs['EventType']]
        self.entity_type = entity_type[kwargs['EntityType']]

    def __str__(self):
        return 'identifier={0}, occurred_on={1}, event_type={2}'.format(
            self.identifier, self.occurred_on, self.event_type)


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
