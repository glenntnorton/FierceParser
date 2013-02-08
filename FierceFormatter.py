# FierceFormatter.py

class FierceFormatter(object):
    def __init__(self):
        pass
    
    def formatFierceScanAttributes(self, l):
        _tmp = {}
        for item in l:
            _tmp[ item[0] ] = item[1]

        return _tmp
        
    def formatDomainScanAttributes(self, l):
        _tmp = {}
        for item in l:
            _tmp[ item[0] ] = item[1]

        return _tmp

    def formatArinAttributes(self, l):
        _tmp = {}
        for item in l:
            _tmp[ item[0] ] = item[1]

        return _tmp

    def formatNameServerAttributes(self, l):
        _tmp = {}
        for item in l:
            _tmp[ item[0] ] = item[1]

        return _tmp

    def formatNameServerNodes(self, l):
        _tmp = {}
        for item in l:
            _tmp[ item[0] ] = item[1]

        return _tmp

    def formatZoneTransferAttributes(self, l):
        _tmp = {}
        for item in l:
            _tmp[ item[0] ] = item[1]

        return _tmp

    def formatZoneTransferRawOutput(self, zt):
        out = []
        for transfer in zt:
            zones = transfer.fetch('zonetransfer')
            for zone in zones:
                outputs = zone.fetch('rawoutput')
                if outputs:
                    out.append(outputs[0].renderContents())
        return out

    def formatZoneTransferNodes(self, zt):
        for transfer in zt:
            zones = transfer.fetch('zonetransfer')
            for zone in zones:
                nodes = zone.fetch('nodes')
                for node in nodes:
                    ns = node.fetch('node')
                    for n in ns:
                        return self.n.attrs
