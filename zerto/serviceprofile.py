# -*- coding: utf-8 -*-
'''Zerto ServiceProfile object'''

from zertoobject import ZertoObject


class ServiceProfile(ZertoObject):

    def __init__(self, **kwargs):
        self.values = kwargs
        self.name = kwargs['ServiceProfileName']
        self.identifier = kwargs['ServiceProfileIdentifier']
        self.description = kwargs.get('Description')
        self.priority = kwargs.get('Priority')
        self.rpo = kwargs.get('Rpo')
        self.test_interval = kwargs.get('TestInterval')
        self.history = kwargs.get('History')
        self.journal_warning_threshold = kwargs.get(
            'JournalWarningThresholdInPercent')
        self.max_journal_size = kwargs.get('MaxJournalSizeInPercent')

    def __str__(self):
        return (
            'name={0}, identifier={1}, description={2}, priority={3}'
        ).format(self.name, self.identifier, self.description, self.priority)


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
