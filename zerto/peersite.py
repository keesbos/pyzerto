# -*- coding: utf-8 -*-
'''Zerto PeerSite object'''

from zertoobject import ZertoObject


class PeerSite(ZertoObject):

    def __init__(self, **kwargs):
        self.values = kwargs
        self.name = kwargs['PeerSiteName']
        self.identifier = kwargs['SiteIdentifier']
        self.version = kwargs.get('Version')
        self.location = kwargs.get('Location')
        self.hostname = kwargs.get('HostName')
        self.port = kwargs.get('Port')
        self.pairing_status = kwargs.get('PairingStatus')
        self.incoming_throughput = kwargs.get('IncomingThroughputInMb')
        self.outgoing_bandwidth = kwargs.get('OutgoingBandWidth')
        self.provisioned_storage = kwargs.get('ProvisionedStorage')
        self.used_storage = kwargs.get('UsedStorage')

    def __str__(self):
        return 'name={0}, identifier={1}, version={2}'.format(
            self.name, self.identifier, self.version)


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
