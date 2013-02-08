#!/usr/bin/env python

# testfp.py
import FierceParser
import FierceFormatter

formatter = FierceFormatter.FierceFormatter()

parser = FierceParser.FierceParser()
parser.setFilename(r'D:\Lib\nc.xml')
parser.parse()

#attrs = parser.getFierceScanAttributes()
#print attrs
#
#print "******"

print 'Basic Scan Information'
d = formatter.formatFierceScanAttributes(parser.getFierceScanAttributes())
for k, v in d.items():
    print k, '==>', v

print "******\n"

#attrs = parser.getDomainScanAttributes()
#print attrs
print 'Basic Domain Information'
d = formatter.formatFierceScanAttributes(parser.getDomainScanAttributes())
for k, v in d.items():
    print k, '==>', v
print "******\n"
#
#attrs = parser.getArinAttributes()
#print attrs
print 'Basic Arin Domain Information'
d = formatter.formatArinAttributes(parser.getArinAttributes())
for k, v in d.items():
    print k, '==>', v
print "******\n"
#
#attrs = parser.getNameServersAttributes()
#print attrs
print 'Name Server Attributes'
d = formatter.formatNameServerAttributes(parser.getNameServersAttributes())
for k, v in d.items():
    print k, '==>', v
print "******\n"

#nodes = parser.getNameServersNodes()
#for node in nodes:
#    print node.attrs

print 'Name Server Information'
nodes = parser.getNameServersNodes()
for node in nodes:
    d = formatter.formatNameServerNodes(node.attrs)
    for k, v in d.items():
        print k, '==>', v
    print
print "******\n"
#
#attrs = parser.getZoneTransfersAttributes()
#print attrs
#
print 'Zone Transfer Attributes'
d = formatter.formatZoneTransferAttributes(parser.getZoneTransfersAttributes())
for k, v in d.items():
    print k, '==>', v
print "******\n"

#zonetransfers = parser.getZoneTransfers()
#for transfer in zonetransfers:
#    zones = transfer.fetch('zonetransfer')
#    for zone in zones:
#        outputs = zone.fetch('rawoutput')
#        if outputs:
#            print outputs[0].renderContents()
#            nodes = zone.fetch('nodes')
#            for node in nodes:
#                ns = node.fetch('node')
#                for n in ns:
#                    print n.attrs
#
#print "******"

zonetransfers = parser.getZoneTransfers()
d = formatter.formatZoneTransferRawOutput(zonetransfers)
for o in d:
    print o
print "******\n"


zonetransfers = parser.getZoneTransfers()
for transfer in zonetransfers:
    zones = transfer.fetch('zonetransfer')
    for zone in zones:
        outputs = zone.fetch('rawoutput')
        if outputs:
            print outputs[0].renderContents()
            nodes = zone.fetch('nodes')
            for node in nodes:
                ns = node.fetch('node')
                for n in ns:
                    print n.attrs

print "******"


#attrs = parser.getWildCardAttributes()
#print attrs
#
#print "******"
#
#attrs = parser.getBruteForceAttributes()
#print attrs
#
#print "******"
#
#bruteforce = parser.getBruteForce()
#for brute in bruteforce:
#    nodes = brute.fetch('node')
#    for node in nodes:
#        print node.attrs
#
#print "******"
#
#attrs = parser.getFindMxAttributes()
#print attrs
#
#print "******"
#
#mxrecords = parser.getFindMx()
#for mxrecord in mxrecords:
#    mx = mxrecord.fetch('mx')
#    for m in mx:
#        print m.attrs
#
#print "******"
#
#attrs = parser.getWhoisAttributes()
#print attrs
#
#print "******"
#
#whois = parser.getWhois()
#for who in whois:
#    ranges = who.fetch('range')
#    for _range in ranges:
#        print _range.attrs
#
#print "******"
#
#attrs = parser.getHostNameLookupsAttributes()
#print attrs
#
#print "******"
#
#hostnames = parser.getHostNameLookups()
#for host in hostnames:
#    nodes = host.fetch('node')
#    for node in nodes:
#        print node.attrs
#
#print "******"
