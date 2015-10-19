# -*- coding: utf-8 -*-
'''Zerto Task object'''

from zertoobject import ZertoObject
from misc import parse_timestamp
from constants import task_state, event_type


class Task(ZertoObject):

    def __init__(self, **kwargs):
        self.values = kwargs
        self.identifier = kwargs['TaskIdentifier']
        self.cancellable = kwargs.get('IsCancellable')
        self.started = parse_timestamp(kwargs.get('Started'))
        self.completed = parse_timestamp(kwargs.get('Completed'))
        self.initiated_by = kwargs.get('InitiatedBy')
        self.complete_reason = kwargs.get('CompleteReason')
        self.status = {}
        for k, v in (kwargs.get('Status') or {}).iteritems():
            if k == 'State':
                self.status[k] = task_state.get(v)
            else:
                self.status[k] = v
        self.task_type = event_type.get(kwargs.get('Type'))

    def __str__(self):
        return (
            'identifier={0}, started={1}, completed={2}, '
            'status={{Progress: {3}, State: {4}}}'
        ).format(
            self.identifier, self.started, self.completed,
            self.status.get('Progress'), self.status.get('State'))


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
