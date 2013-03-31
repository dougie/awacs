# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Amazon EC2'
prefix = 'ec2'

ActivateLicense = Action(prefix, 'ActivateLicense')
AllocateAddress = Action(prefix, 'AllocateAddress')
AssociateAddress = Action(prefix, 'AssociateAddress')
AssociateDhcpOptions = Action(prefix, 'AssociateDhcpOptions')
AssociateRouteTable = Action(prefix, 'AssociateRouteTable')
AttachInternetGateway = Action(prefix, 'AttachInternetGateway')
AttachNetworkInterface = Action(prefix, 'AttachNetworkInterface')
AttachVolume = Action(prefix, 'AttachVolume')
AttachVpnGateway = Action(prefix, 'AttachVpnGateway')
AuthorizeSecurityGroupEgress = \
    Action(prefix, 'AuthorizeSecurityGroupEgress')
AuthorizeSecurityGroupIngress = \
    Action(prefix, 'AuthorizeSecurityGroupIngress')
BundleInstance = Action(prefix, 'BundleInstance')
CancelBundleTask = Action(prefix, 'CancelBundleTask')
CancelConversionTask = Action(prefix, 'CancelConversionTask')
CancelExportTask = Action(prefix, 'CancelExportTask')
CancelSpotInstanceRequests = \
    Action(prefix, 'CancelSpotInstanceRequests')
ConfirmProductInstance = Action(prefix, 'ConfirmProductInstance')
CopySnapshot = Action(prefix, 'CopySnapshot')
CreateCustomerGateway = Action(prefix, 'CreateCustomerGateway')
CreateDhcpOptions = Action(prefix, 'CreateDhcpOptions')
CreateImage = Action(prefix, 'CreateImage')
CreateInstanceExportTask = Action(prefix, 'CreateInstanceExportTask')
CreateInternetGateway = Action(prefix, 'CreateInternetGateway')
CreateKeyPair = Action(prefix, 'CreateKeyPair')
CreateNetworkAcl = Action(prefix, 'CreateNetworkAcl')
CreateNetworkAclEntry = Action(prefix, 'CreateNetworkAclEntry')
CreateNetworkInterface = Action(prefix, 'CreateNetworkInterface')
CreatePlacementGroup = Action(prefix, 'CreatePlacementGroup')
CreateRoute = Action(prefix, 'CreateRoute')
CreateRouteTable = Action(prefix, 'CreateRouteTable')
CreateSecurityGroup = Action(prefix, 'CreateSecurityGroup')
CreateSnapshot = Action(prefix, 'CreateSnapshot')
CreateSpotDatafeedSubscription = \
    Action(prefix, 'CreateSpotDatafeedSubscription')
CreateSubnet = Action(prefix, 'CreateSubnet')
CreateTags = Action(prefix, 'CreateTags')
CreateVolume = Action(prefix, 'CreateVolume')
CreateVpc = Action(prefix, 'CreateVpc')
CreateVpnConnection = Action(prefix, 'CreateVpnConnection')
CreateVpnGateway = Action(prefix, 'CreateVpnGateway')
DeactivateLicense = Action(prefix, 'DeactivateLicense')
DeleteCustomerGateway = Action(prefix, 'DeleteCustomerGateway')
DeleteDhcpOptions = Action(prefix, 'DeleteDhcpOptions')
DeleteInternetGateway = Action(prefix, 'DeleteInternetGateway')
DeleteKeyPair = Action(prefix, 'DeleteKeyPair')
DeleteNetworkAcl = Action(prefix, 'DeleteNetworkAcl')
DeleteNetworkAclEntry = Action(prefix, 'DeleteNetworkAclEntry')
DeleteNetworkInterface = Action(prefix, 'DeleteNetworkInterface')
DeletePlacementGroup = Action(prefix, 'DeletePlacementGroup')
DeleteRoute = Action(prefix, 'DeleteRoute')
DeleteRouteTable = Action(prefix, 'DeleteRouteTable')
DeleteSecurityGroup = Action(prefix, 'DeleteSecurityGroup')
DeleteSnapshot = Action(prefix, 'DeleteSnapshot')
DeleteSpotDatafeedSubscription = \
    Action(prefix, 'DeleteSpotDatafeedSubscription')
DeleteSubnet = Action(prefix, 'DeleteSubnet')
DeleteTags = Action(prefix, 'DeleteTags')
DeleteVolume = Action(prefix, 'DeleteVolume')
DeleteVpc = Action(prefix, 'DeleteVpc')
DeleteVpnConnection = Action(prefix, 'DeleteVpnConnection')
DeleteVpnGateway = Action(prefix, 'DeleteVpnGateway')
DeregisterImage = Action(prefix, 'DeregisterImage')
DescribeAddresses = Action(prefix, 'DescribeAddresses')
DescribeAvailabilityZones = Action(prefix, 'DescribeAvailabilityZones')
DescribeBundleTasks = Action(prefix, 'DescribeBundleTasks')
DescribeConversionTasks = Action(prefix, 'DescribeConversionTasks')
DescribeCustomerGateways = Action(prefix, 'DescribeCustomerGateways')
DescribeDhcpOptions = Action(prefix, 'DescribeDhcpOptions')
DescribeExportTasks = Action(prefix, 'DescribeExportTasks')
DescribeImageAttribute = Action(prefix, 'DescribeImageAttribute')
DescribeImages = Action(prefix, 'DescribeImages')
DescribeInstanceAttribute = Action(prefix, 'DescribeInstanceAttribute')
DescribeInstanceStatus = Action(prefix, 'DescribeInstanceStatus')
DescribeInstances = Action(prefix, 'DescribeInstances')
DescribeInternetGateways = Action(prefix, 'DescribeInternetGateways')
DescribeKeyPairs = Action(prefix, 'DescribeKeyPairs')
DescribeLicenses = Action(prefix, 'DescribeLicenses')
DescribeNetworkAcls = Action(prefix, 'DescribeNetworkAcls')
DescribeNetworkInterfaceAttribute = \
    Action(prefix, 'DescribeNetworkInterfaceAttribute')
DescribeNetworkInterfaces = Action(prefix, 'DescribeNetworkInterfaces')
DescribePlacementGroups = Action(prefix, 'DescribePlacementGroups')
DescribeRegions = Action(prefix, 'DescribeRegions')
DescribeReservedInstances = Action(prefix, 'DescribeReservedInstances')
DescribeReservedInstancesOfferings = \
    Action(prefix, 'DescribeReservedInstancesOfferings')
DescribeRouteTables = Action(prefix, 'DescribeRouteTables')
DescribeSecurityGroups = Action(prefix, 'DescribeSecurityGroups')
DescribeSnapshotAttribute = Action(prefix, 'DescribeSnapshotAttribute')
DescribeSnapshots = Action(prefix, 'DescribeSnapshots')
DescribeSpotDatafeedSubscription = \
    Action(prefix, 'DescribeSpotDatafeedSubscription')
DescribeSpotInstanceRequests = \
    Action(prefix, 'DescribeSpotInstanceRequests')
DescribeSpotPriceHistory = Action(prefix, 'DescribeSpotPriceHistory')
DescribeSubnets = Action(prefix, 'DescribeSubnets')
DescribeTags = Action(prefix, 'DescribeTags')
DescribeVolumeAttribute = Action(prefix, 'DescribeVolumeAttribute')
DescribeVolumeStatus = Action(prefix, 'DescribeVolumeStatus')
DescribeVolumes = Action(prefix, 'DescribeVolumes')
DescribeVpcs = Action(prefix, 'DescribeVpcs')
DescribeVpnConnections = Action(prefix, 'DescribeVpnConnections')
DescribeVpnGateways = Action(prefix, 'DescribeVpnGateways')
DetachInternetGateway = Action(prefix, 'DetachInternetGateway')
DetachNetworkInterface = Action(prefix, 'DetachNetworkInterface')
DetachVolume = Action(prefix, 'DetachVolume')
DetachVpnGateway = Action(prefix, 'DetachVpnGateway')
DisassociateAddress = Action(prefix, 'DisassociateAddress')
DisassociateRouteTable = Action(prefix, 'DisassociateRouteTable')
EnableVolumeIO = Action(prefix, 'EnableVolumeIO')
GetConsoleOutput = Action(prefix, 'GetConsoleOutput')
GetPasswordData = Action(prefix, 'GetPasswordData')
ImportInstance = Action(prefix, 'ImportInstance')
ImportKeyPair = Action(prefix, 'ImportKeyPair')
ImportVolume = Action(prefix, 'ImportVolume')
ModifyImageAttribute = Action(prefix, 'ModifyImageAttribute')
ModifyInstanceAttribute = Action(prefix, 'ModifyInstanceAttribute')
ModifyNetworkInterfaceAttribute = \
    Action(prefix, 'ModifyNetworkInterfaceAttribute')
ModifySnapshotAttribute = Action(prefix, 'ModifySnapshotAttribute')
ModifyVolumeAttribute = Action(prefix, 'ModifyVolumeAttribute')
MonitorInstances = Action(prefix, 'MonitorInstances')
PurchaseReservedInstancesOffering = \
    Action(prefix, 'PurchaseReservedInstancesOffering')
RebootInstances = Action(prefix, 'RebootInstances')
RegisterImage = Action(prefix, 'RegisterImage')
ReleaseAddress = Action(prefix, 'ReleaseAddress')
ReplaceNetworkAclAssociation = \
    Action(prefix, 'ReplaceNetworkAclAssociation')
ReplaceNetworkAclEntry = Action(prefix, 'ReplaceNetworkAclEntry')
ReplaceRoute = Action(prefix, 'ReplaceRoute')
ReplaceRouteTableAssociation = \
    Action(prefix, 'ReplaceRouteTableAssociation')
ReportInstanceStatus = Action(prefix, 'ReportInstanceStatus')
RequestSpotInstances = Action(prefix, 'RequestSpotInstances')
ResetImageAttribute = Action(prefix, 'ResetImageAttribute')
ResetInstanceAttribute = Action(prefix, 'ResetInstanceAttribute')
ResetNetworkInterfaceAttribute = \
    Action(prefix, 'ResetNetworkInterfaceAttribute')
ResetSnapshotAttribute = Action(prefix, 'ResetSnapshotAttribute')
RevokeSecurityGroupEgress = Action(prefix, 'RevokeSecurityGroupEgress')
RevokeSecurityGroupIngress = \
    Action(prefix, 'RevokeSecurityGroupIngress')
RunInstances = Action(prefix, 'RunInstances')
StartInstances = Action(prefix, 'StartInstances')
StopInstances = Action(prefix, 'StopInstances')
TerminateInstances = Action(prefix, 'TerminateInstances')
UnmonitorInstances = Action(prefix, 'UnmonitorInstances')