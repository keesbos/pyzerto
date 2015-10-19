# -*- coding: utf-8 -*-
'''Zerto protected VM object'''

from zertoobject import ZertoObject
from constants import vpg_status, vpg_sub_status, vpg_priority, site_type


class VM(ZertoObject):

    def __init__(self, **kwargs):
        self.values = kwargs
        self.name = kwargs['VmName']
        self.identifier = kwargs['VmIdentifier']
        self.vpg_name = kwargs['VpgName']
        self.organization_name = kwargs['OrganizationName']
        self.status = vpg_status[kwargs['Status']]
        self.sub_status = vpg_sub_status[kwargs['SubStatus']]
        self.priority = vpg_priority[kwargs['Priority']]
        self.source_site = kwargs.get('SourceSite')
        self.target_site = kwargs.get('TargetSite')
        self.actual_rpo = kwargs.get('ActualRPO')
        self.provisioned_storage = kwargs.get('ProvisionedStorageInMB')
        self.used_storage = kwargs.get('UsedStorageInMB')
        self.throughput = kwargs.get('ThroughputInMB')
        self.iops = kwargs.get('IOPS')
        self.last_test = kwargs.get('LastTest')
        self.entities = {}
        for k, v in (kwargs.get('Entities') or {}).iteritems():
            self.entities[k] = site_type[v]

    def __str__(self):
        return 'name={0}, identifier={1}, status={2}, sub_status={3}'.format(
            self.name, self.identifier, self.status, self.sub_status)


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
