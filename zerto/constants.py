# -*- coding: utf-8 -*-
'''
Module with zerto constants
'''


class ZertoConstant(object):

    def __init__(self, code, name, descr=''):
        self.code = code
        self.name = name
        self.descr = descr

    def __str__(self):
        return '({0}, {1})'.format(self.code, self.name)


class ZertoConstantDict(dict):

    def __init__(self, constants, constant_class=ZertoConstant):
        super(ZertoConstantDict, self).__init__(self)
        if not isinstance(constants, list):
            constants = [constants]
        for constant in constants:
            if not isinstance(constant, constant_class):
                constant = constant_class(*constant)
            self[constant.code] = self[constant.name] = constant


class AuthenticationMethod(ZertoConstant):
    pass


authentication_method = ZertoConstantDict([
    (0, 'Windows', (
        'Authentication requires the username and password to access the '
        'machine where the Zerto Virtual Manager is installed and where the '
        'APIs will run. Windows authentication is the default if '
        'AuthenticationMethod is not set.')),
    (1, 'VirtualizationManager', (
        'Authentication requires the username and password to access the '
        'VMware vCenter Server or Microsoft SCVMM accessed by the Zerto '
        'Virtual Manager where the APIs will run.')),
], AuthenticationMethod)


class CommitPolicy(ZertoConstant):
    pass


commit_policy = ZertoConstantDict([
    (0, 'rollback', (
        'After the seconds specified in the commitValue setting '
        'have elapsed, the failover is rolled back.')),
    (1, 'commit', (
        'After the seconds specified in the commitValue setting '
        'have elapsed, the failover continue, committing the virtual '
        'machines in the recovery site.')),
    (2, 'none', (
        'The virtual machines in the VPG being failed over remain '
        'in the Before Commit state until either they are committed with '
        'Commit a failover, or rolled back with Roll back a failover.')),
], CommitPolicy)


class EntityType(ZertoConstant):
    pass


entity_type = ZertoConstantDict([
    (0, 'VPG', 'The entity is a VPG.'),
    (1, 'VRA', 'The entity is a VRA.'),
    (2, 'Unknown', 'The entity is unknown.'),
    (3, 'Site', 'The entity is the site.'),
], EntityType)


class EventCategory(ZertoConstant):
    pass


event_category = ZertoConstantDict([
    (0, 'All', 'All event types.'),
    (1, 'Events', 'The event is not an alert event (not EV0056 nor EV0057).'),
    (2, 'Alerts', 'The event is an alert event (EV0056 and EV0057)'),
], EventCategory)


class EventType(ZertoConstant):
    pass


event_type = ZertoConstantDict([
    (0, 'Unknown'),
    (1, 'CreateProtectionGroup'),
    (2, 'RemoveProtectionGroup'),
    (3, 'FailOver'),
    (4, 'FailOverTest'),
    (5, 'StopFailOverTest'),
    (6, 'Move'),
    (7, 'ProtectVM'),
    (8, 'UnprotectVM'),
    (9, 'InstallVra'),
    (10, 'UninstallVra'),
    (11, 'UpdateProtectionGroup'),
    (12, 'InsertTaggedCP'),
    (13, 'HandleMirrorPromotion'),
    (14, 'ActivateAllMirrors'),
    (15, 'LogCollection'),
    (16, 'ForceReconfigurationOfNewVM'),
    (17, 'ClearSite'),
    (18, 'ForceRemoveProtectionGroup'),
    (19, 'ForceUpdateProtectionGroup'),
    (20, 'ForceKillProtectionGroup'),
    (21, 'PrePostScript'),
    (22, 'InitFullSync'),
    (23, 'Pair'),
    (24, 'Unpair'),
    (25, 'InstallCloudConnector'),
    (26, 'UninstallCloudConnector'),
    (27, 'RedeployCloudConnector'),
    (28, 'ScriptExecutionFailure'),
    (29, 'SetAdvancedSiteSettings'),
    (30, 'Clone'),
    (31, 'KeepDisk'),
    (32, 'FailoverBeforeCommit'),
    (33, 'FailoverCommit'),
    (34, 'FailoverRollback'),
    (35, 'MoveBeforeCommit'),
    (36, 'MoveRollback'),
    (37, 'MoveCommit'),
    (38, 'MaintainHost'),
    (39, 'UpgradeVra'),
    (40, 'MoveProtectionGroupToManualOperationNeeded'),
    (41, 'ChangeVraIpSettings'),
    (42, 'PauseProtectionGroup'),
    (43, 'ResumeProtectionGroup'),
    (44, 'UpgradeZVM'),
    (45, 'BulkUpgradeVras'),
    (46, 'BulkUninstallVras'),
    (47, 'AlertTurnedOn'),
    (48, 'AlertTurnedOff'),
    (49, 'ChangeVraPassword'),
    (50, 'ChangeRecoveryHost'),
    (51, 'BackupProtectionGroup'),
    (52, 'CleanupProtectionGroupVipDiskbox'),
    (53, 'RestoreProtectionGroup'),
    (54, 'PreScript'),
    (55, 'PostScript'),
    (56, 'RemoveVmFromVc'),
    (57, 'ChangeVraPasswordIpSettings'),
    (58, 'FlrJournalMount'),
    (59, 'FlrJournalUnmount'),
    (60, 'Login'),
    (61, 'HostEnteringMaintenanceMode'),
    (62, 'HostExitingMaintenanceMode'),
    (63, 'VmRestoredToSnapshot'),
    (64, 'ProtectedVmRemovedFromHypervisor'),
    (65, 'ProtectedVmAddedToHypervisor'),
    (66, 'PauseProtectionGroupForMissingVm'),
    (67, 'ResumeProtectionGroupAfterUserRemovedMissingVm'),
    (68, 'ResumeProtectionGroupAfterVmReadded'),
], EventType)


class PairingStatus(ZertoConstant):
    pass


pairing_status = ZertoConstantDict([
    (0, 'Paired', 'The site is paired.'),
    (1, 'Pairing', 'The site is in the process of being paired.'),
    (2, 'Unpaired', 'The site is not paired.'),
], PairingStatus)


class SiteType(ZertoConstant):
    pass


site_type = ZertoConstantDict([
    (0, 'VCVpg', 'The VPG is protecting/recovering virtual machines in a '
        'VMware vCenter Server.'),
    (1, ' VCvApp', 'The VPG is protecting/recovering a VMware vCenter Server '
        'vApp.'),
    (2, ' VCDvApp', 'The VPG is protecting/recovering a VMware vCloud '
        'Director vApp.'),
    (3, 'PublicCloud', 'Not applicable.'),
    (4, 'HyperV', 'The VPG is protecting/recovering virtual machines in '
        'Microsoft Hyper-V.'),
], SiteType)


class TaskState(ZertoConstant):
    pass


task_state = ZertoConstantDict([
    (0, 'FirstUnusedValue'),
    (1, 'InProgress'),
    (2, 'WaitingForUserInput'),
    (3, 'Paused'),
    (4, 'Failed'),
    (5, 'Stopped'),
    (6, 'Completed'),
    (7, 'Cancelling'),
], TaskState)


class VMType(ZertoConstant):
    pass


vm_type = ZertoConstantDict([
    (0, 'VCVpg', 'Virtual machines in a VMware vCenter Server.'),
    (1, 'VCvApp', 'VMware vCenter Server vApp.'),
    (2, 'VCDvApp', 'VMware vCloud Director vApp.'),
    (3, 'PublicCloud', 'Not applicable.'),
    (4, 'HyperV', 'Virtual machines in Microsoft Hyper-V.'),
], VMType)


class VPGPriority(ZertoConstant):
    pass


vpg_priority = ZertoConstantDict([
    (0, 'Low', 'The VPG has a high priority for transferring data.'),
    (1, 'Medium', 'The VPG has a medium priority for transferring data.'),
    (2, 'High', 'The VPG has a low priority for transferring data.'),
], VPGPriority)


class VPGStatus(ZertoConstant):
    pass


vpg_status = ZertoConstantDict([
    (0, 'Initializing', 'The VPG is being initialized. This includes when '
        'a VPG is created, and the initial sync between sites.'),
    (1, 'MeetingSLA', 'The VPG is meeting the SLA specification.'),
    (2, 'NotMeetingSLA', 'The VPG is not meeting the SLA specification for '
        'both the journal history and RPO SLA settings.'),
    (3, 'RpoNotMeetingSLA', 'The VPG is not meeting the SLA specification '
        'for the RPO SLA setting.'),
    (4, 'HistoryNotMeetingSLA', 'The VPG is not meeting the SLA '
        'specification for the journal history.'),
    (5, 'FailingOver', 'The VPG is in a Failover operating.'),
    (6, 'Moving', 'The VPG is in a Move operation.'),
    (7, 'Deleting', 'The VPG is being deleted.'),
], VPGStatus)


class VPGSubStatus(ZertoConstant):
    pass


vpg_sub_status = ZertoConstantDict([
    (0, 'None'),
    (1, 'InitialSync'),
    (2, 'Creating'),
    (3, 'VolumeInitialSync'),
    (4, 'Sync'),
    (5, 'RecoveryPossible'),
    (6, 'DeltaSync'),
    (7, 'NeedsConfiguration'),
    (8, 'Error'),
    (9, 'EmptyProtectionGroup'),
    (10, 'DisconnectedFromPeerNoRecoveryPoints'),
    (11, 'FullSync'),
    (12, 'VolumeDeltaSync'),
    (13, 'VolumeFullSync'),
    (14, 'FailingOverCommitting'),
    (15, 'FailingOverBeforeCommit'),
    (16, 'FailingOverRollingBack'),
    (17, 'Promoting'),
    (18, 'MovingCommitting'),
    (19, 'MovingBeforeCommit'),
    (20, 'MovingRollingBack'),
    (21, 'Deleting'),
    (22, 'PendingRemove'),
    (23, 'BitmapSync'),
    (24, 'DisconnectedFromPeer'),
    (25, 'ReplicationPausedUserInitiated'),
    (26, 'ReplicationPausedSystemInitiated'),
    (27, 'RecoveryStorageProfileError'),
    (28, 'Backup'),
    (29, 'RollingBack'),
    (30, 'RecoveryStorageError'),
    (31, 'JournalStorageError'),
    (32, 'VmNotProtectedError'),
], VPGSubStatus)


class VRAStatus(ZertoConstant):
    pass


vra_status = ZertoConstantDict([
    (0, 'Installed', 'The VRA is installed.'),
    (1, 'UnsupportedEsxVersion', 'The VRA cannot be installed on the '
        'ESX/ESXi host as the host version is not supported.'),
    (2, 'NotInstalled', 'A VRA is not installed.'),
    (3, 'Installing', 'The VRA is being installed.'),
    (4, 'Removing', 'The VRA is being removed.'),
    (5, 'InstallationError', 'The installation of the VRA failed.'),
    (6, 'HostPasswordChanged', 'The password used to access the host has '
        'changed.'),
    (7, 'UpdatingIpSettings', 'The IP settings of the VRA are updated.'),
    (8, 'DuringChangeHost', 'The host of the VRA disks is being changed.'),
], VRAStatus)


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
