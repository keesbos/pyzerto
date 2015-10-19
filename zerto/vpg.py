# -*- coding: utf-8 -*-
'''Zerto VPG object'''

from zertoobject import ZertoObject
from constants import vpg_status, vpg_sub_status


class VPG(ZertoObject):

    def __init__(self, **kwargs):
        self.values = kwargs
        self.name = kwargs['VpgName']
        self.identifier = kwargs['VpgIdentifier']
        self.status = vpg_status[kwargs['Status']]
        self.sub_status = vpg_sub_status[kwargs['SubStatus']]
        self.priority = kwargs.get('Priority')
        self.source_site = kwargs.get('SourceSite')
        self.target_site = kwargs.get('TargetSite')
        self.actual_rpo = kwargs.get('ActualRPO')
        self.vms_count = kwargs.get('VmsCount')
        self.progress_percentage = kwargs.get('ProgressPercentage')
        self.provisioned_storage = kwargs.get('ProvisionedStorageInMB')
        self.used_storage = kwargs.get('UsedStorageInMB')

    def __str__(self):
        return 'name={0}, identifier={1}, status={2}, sub_status={3}'.format(
            self.name, self.identifier, self.status, self.sub_status)


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
