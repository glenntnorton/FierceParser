from com.finnean.io.reader import FileReader
from com.finnean.io.parser._lib import BeautifulSoup

class FierceParser(object):
    def __init__(self, filename=None):
        self.filename = filename
        self.reader = None
        self.parser = None
    
    def setFilename(self, f):
        self.filename = f

    def parse(self):
        self.reader = FileReader.FileReader(self.filename)
        self.parser = BeautifulSoup.BeautifulSoup()
        self.parser.feed(self.reader.read())
    
    def getFierceScanAttributes(self):
        a = self.parser.fetch('fiercescan')
        return a[0].attrs

    def getDomainScanAttributes(self):
        a = self.parser.fetch('domainscan')
        return a[0].attrs

    def getArinAttributes(self):
        a = self.parser.fetch('arin')
        return a[0].attrs

    def getNameServersAttributes(self):
        a = self.parser.fetch('nameservers')
        return a[0].attrs

    def getNameServersNodes(self):
        n = self.parser.fetch('nameservers')
        return n[0].fetch('node')


    def getZoneTransfersAttributes(self):
        a = self.parser.fetch('zonetransfers')
        return a[0].attrs

    def getZoneTransfers(self):
        return self.parser.fetch('zonetransfers')


    def getWildCardAttributes(self):
        a = self.parser.fetch('wildcard')
        return a[0].attrs


    def getBruteForceAttributes(self):
        a = self.parser.fetch('bruteforce')
        return a[0].attrs

    def getBruteForce(self):
        return self.parser.fetch('bruteforce')


    def getFindMxAttributes(self):
        a = self.parser.fetch('findmx')
        return a[0].attrs

    def getFindMx(self):
        return self.parser.fetch('findmx')

    def getWhoisAttributes(self):
        a = self.parser.fetch('whois')
        return a[0].attrs

    def getWhois(self):
        return self.parser.fetch('whois')

    def getHostNameLookupsAttributes(self):
        a = self.parser.fetch('hostnamelookups')
        return a[0].attrs

    def getHostNameLookups(self):
        return self.parser.fetch('hostnamelookups')

