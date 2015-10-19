# -*- coding: utf-8 -*-
'''Zerto VRA object'''

from zertoobject import ZertoObject
from constants import vra_status


class VRA(ZertoObject):

    def __init__(self, **kwargs):
        self.values = kwargs
        self.name = kwargs['VraName']
        self.identifier = kwargs['VraIdentifier']
        self.status = vra_status[kwargs['Status']]
        self.vra_version = kwargs.get('VraVersion')
        self.vra_group = kwargs.get('VraGroup')
        self.ipaddress = kwargs.get('IpAddress')
        self.host_version = kwargs.get('HostVersion')
        self.network_name = kwargs.get('NetworkName')
        self.datastore_cluster_name = kwargs.get('DatastoreClusterName')
        self.datastore_name = kwargs.get('DatastoreName')
        self.self_protected_vgs = kwargs.get('SelfProtectedVpgs')
        self.progress = kwargs.get('Progress')
        self.memory = kwargs.get('MemoryInGB')
        self.protected_counters = {}
        self.protected_counters.update(kwargs.get('ProtectedCounters') or {})
        self.recovery_counters = {}
        self.recovery_counters.update(kwargs.get('RecoveryCounters') or {})

    def __str__(self):
        return 'name={0}, identifier={1}, vra_group={2}, status={3}'.format(
            self.name, self.identifier, self.vra_group, self.status)


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
